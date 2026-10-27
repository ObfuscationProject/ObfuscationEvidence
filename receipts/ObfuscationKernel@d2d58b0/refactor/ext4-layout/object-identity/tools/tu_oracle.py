#!/usr/bin/env python3
"""Compile unchanged baseline test TUs against the baseline headers and against the
folded headers (through old-path shims); compare the generated code.

usage: tu_oracle.py <baseline-tree> <new-tree> <out> <jobs> [<units-file>]

With a units file, only those units are compiled again and their entries in
<out>/results.json are replaced.
"""
import concurrent.futures
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from assign import MODULES  # noqa: E402

base, new, out, jobs = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), int(sys.argv[4])
only = Path(sys.argv[5]).read_text().split() if len(sys.argv) > 5 else None
out.mkdir(parents=True, exist_ok=True)
shim = out / "shim"
for module, names in MODULES.items():
    for name in names:
        path = shim / "ok/fs" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'#pragma once\n#include "ok/fs/ext4/{module}.hpp"\n')

SLICE = re.compile(r'ok/fs/(ext4|jbd2|metadata_buffers)')
units = []
for d in ("tests/host", "tests/native", "tests/fixtures", "tests/kernel"):
    for p in sorted((base / d).rglob("*.cpp")):
        units.append(p)

FLAGS = ["-std=c++23", "-O2", "-fno-exceptions", "-frtti", "-w", "-DOK_ARCH_TARGET_X86_64"]


def compile_one(unit: Path):
    rel = unit.relative_to(base)
    tag = str(rel).replace("/", "__")
    # Only units that reach an ext4 slice through any include path.
    dep = subprocess.run(["g++", *FLAGS, "-I" + str(base / "include"), "-I" + str(base / "tests/host"), "-M", str(unit)],
                         capture_output=True, text=True, cwd=unit.parent)
    if dep.returncode != 0:
        return str(rel), "base-preprocess-fail", ""
    if not SLICE.search(dep.stdout):
        return str(rel), "unrelated", ""
    results = {}
    for side, incs in (("base", [base / "include"]), ("new", [new / "include", shim])):
        obj = out / side / (tag + ".o")
        obj.parent.mkdir(parents=True, exist_ok=True)
        extra = []
        for attempt in ([], ["-fno-access-control"]):
            cmd = ["g++", *FLAGS, *attempt, *("-I" + str(i) for i in incs), "-I" + str(base / "tests/host"), "-c", str(unit), "-o", str(obj)]
            r = subprocess.run(cmd, capture_output=True, text=True, cwd=unit.parent)
            if r.returncode == 0:
                extra = attempt
                break
        results[side] = (r.returncode, extra, r.stderr[-2000:])
    b, n = results["base"], results["new"]
    if b[0] != 0 and n[0] != 0:
        return str(rel), "both-fail", ""
    if b[0] != 0:
        return str(rel), "base-fail-new-ok", b[2]
    if n[0] != 0:
        return str(rel), "NEW-FAIL", n[2]
    if b[1] != n[1]:
        return str(rel), "ACCESS-CONTROL-DIFFERS", ""
    ob, on = (out / s / (tag + ".o") for s in ("base", "new"))
    if ob.read_bytes() == on.read_bytes():
        return str(rel), "identical", ""
    def norm(o):
        text = subprocess.run(["objdump", "-d", "-r", "--no-show-raw-insn", "-j", ".text", str(o)], capture_output=True, text=True).stdout
        funcs, cur = {}, None
        for line in text.splitlines():
            m = re.match(r"^[0-9a-f]+ <(.+)>:$", line)
            if m:
                cur = m.group(1); funcs[cur] = []
            elif cur and line.strip():
                funcs[cur].append(re.sub(r"^\s*[0-9a-f]+:\s*", "", line))
        return funcs
    fb, fn = norm(ob), norm(on)
    if fb == fn:
        return str(rel), "same-code", ""
    diff = sorted(k for k in set(fb) | set(fn) if fb.get(k) != fn.get(k))
    return str(rel), "CODE-DIFFERS", "\n".join(diff[:20])


if only is not None:
    units = [u for u in units if str(u.relative_to(base)) in only]
results = json.loads((out / "results.json").read_text()) if only is not None else {}
with concurrent.futures.ThreadPoolExecutor(jobs) as pool:
    for rel, state, detail in pool.map(compile_one, units):
        results[rel] = [state, detail]
        if state not in ("unrelated",):
            print(state, rel, flush=True)
(out / "results.json").write_text(json.dumps(results, indent=1))
summary = {}
for state, _ in results.values():
    summary[state] = summary.get(state, 0) + 1
print(json.dumps(summary, indent=1))
