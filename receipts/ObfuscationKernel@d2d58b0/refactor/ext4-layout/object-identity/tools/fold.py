#!/usr/bin/env python3
"""One-shot migration: fold the ext4/JBD2 slice headers of include/ok/fs into the
eight module headers under include/ok/fs/ext4/, move the private partial class
bodies to include/ok/fs/ext4/detail/, and rewrite every consumer include.

usage: fold.py <kernel-root> [--consumers-only <root>...]
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from assign import KEEP, MODULES, ORDER  # noqa: E402

DESCRIPTIONS = {
    "journal": "JBD2 on-disk records, the bounded journal replay executor and the ext4\n"
               "// journal recovery binding.",
    "layout": "ext4 superblock and inode layout, timestamps, block accounting, the\n"
              "// checked read-only view and the VFS filesystem.",
    "extent": "extent-backed data planning: first and next data blocks, zero-length\n"
              "// truncate and allocated-empty data, with their witnesses, previews and journal\n"
              "// records.",
    "alloc": "inode allocation and lifetime, regular and directory create plans, orphan\n"
             "// chains and orphan reclaim planning.",
    "dir": "directory namespace, rename and regular-file move plans, witnesses and journal\n"
           "// records.",
    "txn": "final journal replay view, recovery completion, metadata buffers and the\n"
           "// metadata transaction with its per-mutation writers.",
    "recovery": "cold replay, recovery bindings and completion of interrupted namespace,\n"
                "// regular-move and reclaim mutations, their result histories and the orphan-chain\n"
                "// capture.",
    "mount": "mounted typed cursors and budgets, the owned transaction, empty-orphan\n"
             "// recovery and the mounted metadata provider.",
}

INCLUDE = re.compile(r'^(\s*)#include ([<"])ok/fs/([^">]+)([">])(.*)$')


def is_slice(name: str) -> bool:
    return "/" not in name and name not in KEEP and (name.startswith(("ext4", "jbd2")) or name == "metadata_buffers.hpp")


def detail_name(inc: str) -> str:
    stem = inc[len("ext4_"):] if inc.startswith("ext4_") else inc
    return "ext4/detail/" + stem


def module_of() -> dict[str, str]:
    return {f: m for m, files in MODULES.items() for f in files}


def split_header(text: str, name: str):
    """Return (top slice includes, top external include lines, body lines, tail slice includes)."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    top_slices, externals, body = [], [], []
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped in ("", "#pragma once"):
            index += 1
            continue
        if stripped.startswith("#include"):
            match = INCLUDE.match(line)
            if match and is_slice(match.group(3)):
                assert not match.group(3).endswith(".inc"), (name, line)
                top_slices.append(match.group(3))
            else:
                externals.append(stripped)
            index += 1
            continue
        break
    body = lines[index:]
    tail = []
    # Includes after code: only slice includes are allowed (deferred definitions).
    kept = []
    for line in body:
        match = INCLUDE.match(line)
        if match and is_slice(match.group(3)) and not match.group(3).endswith(".inc") and not match.group(1):
            tail.append(match.group(3))
            continue
        assert not (line.strip().startswith("#include") and not match), (name, line)
        if match and match.group(3).endswith(".inc"):
            line = f'{match.group(1)}#include "ok/fs/{detail_name(match.group(3))}"{match.group(5)}'
        elif match and is_slice(match.group(3)):
            raise AssertionError((name, line))
        kept.append(line)
    while kept and kept[-1].strip() == "":
        kept.pop()
    return top_slices, externals, kept, tail


def topo_order(module: str, parsed) -> list[str]:
    members = MODULES[module]
    rank = {name: index for index, name in enumerate(members)}
    before = {name: set() for name in members}  # name -> members that must precede it
    for name in members:
        top, _, _, tail = parsed[name]
        for dep in top:
            if dep in rank:
                before[name].add(dep)
        for dep in tail:
            if dep in rank:
                before[dep].add(name)
    order, done = [], set()
    while len(order) < len(members):
        ready = [n for n in members if n not in done and before[n] <= done]
        assert ready, (module, [n for n in members if n not in done])
        pick = min(ready, key=rank.__getitem__)
        order.append(pick)
        done.add(pick)
    return order


def merge_bodies(bodies: list[list[str]]) -> list[str]:
    out: list[str] = []
    for body in bodies:
        if out:
            last = len(out) - 1
            while last >= 0 and out[last].strip() == "":
                last -= 1
            first = 0
            while first < len(body) and body[first].strip() == "":
                first += 1
            closing = out[last].strip() if last >= 0 else ""
            m = re.fullmatch(r"\} // namespace ([A-Za-z0-9_:]+)", closing)
            opening = 0
            if m and first < len(body) and body[first].strip() == f"namespace {m.group(1)} {{":
                opening = 1
            elif (m and first + 1 < len(body) and body[first].strip() == f"namespace {m.group(1)}"
                    and body[first + 1].strip() == "{"):
                opening = 2
            if opening:
                del out[last:]
                body = body[first + opening:]
                while body and body[0].strip() == "":
                    body = body[1:]
                out.append("")
            else:
                out.append("")
        out.extend(body)
    return out


def fold(root: Path) -> None:
    fs = root / "include/ok/fs"
    owner = module_of()
    names = sorted(p.name for p in fs.iterdir() if p.is_file() and is_slice(p.name))
    headers = [n for n in names if n.endswith(".hpp")]
    partials = [n for n in names if n.endswith(".inc")]
    assert sorted(owner) == headers, set(owner) ^ set(headers)
    parsed = {n: split_header((fs / n).read_text(), n) for n in headers}
    rank = {m: i for i, m in enumerate(ORDER)}
    deps: dict[str, set[str]] = {m: set() for m in ORDER}
    for name in headers:
        for dep in parsed[name][0] + parsed[name][3]:
            if owner[dep] != owner[name]:
                assert rank[owner[dep]] < rank[owner[name]], (name, dep)
                deps[owner[name]].add(owner[dep])
    for module in ORDER:
        order = topo_order(module, parsed)
        externals: list[str] = []
        for name in order:
            for line in parsed[name][1]:
                if line not in externals:
                    externals.append(line)
        project = [e for e in externals if e.startswith('#include "')]
        system = [e for e in externals if e.startswith("#include <")]
        lines = ["#pragma once", "", f"// ext4 {module} module: {DESCRIPTIONS[module]}", ""]
        for dep in sorted(deps[module], key=rank.__getitem__):
            lines.append(f'#include "ok/fs/ext4/{dep}.hpp"')
        lines += project
        lines += system
        lines.append("")
        lines += merge_bodies([parsed[n][2] for n in order])
        (fs / "ext4" / f"{module}.hpp").write_text("\n".join(lines) + "\n")
        print(f"{module}: {len(order)} slices, {len(lines)} lines, deps {sorted(deps[module], key=rank.__getitem__)}")
    detail = fs / "ext4/detail"
    detail.mkdir(exist_ok=True)
    for name in partials:
        text = (fs / name).read_text()
        out = []
        for line in text.split("\n"):
            match = INCLUDE.match(line)
            if match:
                assert match.group(3).endswith(".inc"), (name, line)
                line = f'{match.group(1)}#include "ok/fs/{detail_name(match.group(3))}"{match.group(5)}'
            out.append(line)
        (fs / detail_name(name)).write_text("\n".join(out))
    for name in names:
        (fs / name).unlink()


def rewrite_consumers(roots: list[Path], owner: dict[str, str]) -> None:
    suffixes = {".cpp", ".hpp", ".h", ".c", ".inc", ".cc"}
    for base in roots:
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix not in suffixes:
                continue
            if any(part in ("build", ".git", ".xmake") for part in path.relative_to(base).parts):
                continue
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                continue
            if "ok/fs/" not in text:
                continue
            seen: set[str] = set()
            out, changed = [], False
            for line in text.split("\n"):
                match = INCLUDE.match(line)
                if match and match.group(3).startswith("ext4/"):
                    seen.add(match.group(3))
                if match and is_slice(match.group(3)):
                    name = match.group(3)
                    assert name in owner, (path, line)
                    target = f"ext4/{owner[name]}.hpp"
                    changed = True
                    if target in seen:
                        continue
                    seen.add(target)
                    close = ">" if match.group(2) == "<" else '"'
                    line = f"{match.group(1)}#include {match.group(2)}ok/fs/{target}{close}{match.group(5)}"
                out.append(line)
            if changed:
                path.write_text("\n".join(out))
                print("rewrote", path)


def main() -> None:
    root = Path(sys.argv[1]).resolve()
    owner = module_of()
    if "--consumers-only" in sys.argv:
        rewrite_consumers([Path(p).resolve() for p in sys.argv[sys.argv.index("--consumers-only") + 1:]], owner)
        return
    fold(root)
    rewrite_consumers([root / d for d in ("src", "tests", "tools", "include")], owner)


if __name__ == "__main__":
    main()
