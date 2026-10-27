#!/usr/bin/env python3
"""For each kernel configuration, find objects that differ between the baseline and
the new build (debug objects compared with debug info stripped), recompile those
units to assembly with their exact xmake command lines, and compare per symbol.

usage: kasm.py <baseline-tree> <new-tree> <config>...
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).parent
base_tree, new_tree = Path(sys.argv[1]), Path(sys.argv[2])
TRIPLES = {"i386": "i386-elf", "x86_64": "x86_64-elf", "aarch64": "aarch64-elf", "arm32": "arm-none-eabi",
           "rv64": "riscv64-elf", "rv32": "riscv32-elf", "loongarch64": "loongarch64-elf", "mips": "mips-elf",
           "mips64": "mips64-elf", "ppc": "powerpc-eabi"}


def commands(tag, tree, config):
    out = S / f"cc_{tag}_{config}"
    subprocess.run(["xmake", "project", "-P", str(tree), "-k", "compile_commands", str(out)],
                   env={**__import__("os").environ, "XMAKE_CONFIGDIR": str(S / "cfg" / f"{tag}-{config}")},
                   capture_output=True, text=True, check=True)
    entries = {}
    for e in json.loads((out / "compile_commands.json").read_text()):
        target = e["arguments"][e["arguments"].index("-o") + 1]
        entries[target.split(f"/{config}/", 1)[1]] = e
    return entries


def to_asm(entry, asm, opt=None):
    args = list(entry["arguments"])
    i = args.index("-o")
    args[i + 1] = str(asm)
    args = [a for a in args if a != "-c"] + ["-S"]
    args = [a for a in args if not a.startswith("-g")] + ["-g0"]
    if opt:
        args = [a for a in args if not a.startswith("-O")] + [opt]
    r = subprocess.run(args, cwd=entry["directory"], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-800:])


for config in sys.argv[3:]:
    arch = config.rsplit("-", 1)[0]
    objcopy = S / "st" / TRIPLES[arch] / "bin" / (TRIPLES[arch] + "-objcopy")
    bdir, ndir = S / "bld" / "base" / config, S / "bld" / "new" / config
    differing = []
    with tempfile.TemporaryDirectory(dir=S) as tmp:
        for obj in sorted(bdir.rglob("*.o")):
            rel = obj.relative_to(bdir)
            other = ndir / rel
            a, b = Path(tmp) / "a.o", Path(tmp) / "b.o"
            subprocess.run([str(objcopy), "--strip-debug", str(obj), str(a)], check=True)
            subprocess.run([str(objcopy), "--strip-debug", str(other), str(b)], check=True)
            if a.read_bytes() != b.read_bytes():
                differing.append(rel)
    if not differing:
        print(f"{config}: all objects identical", flush=True)
        continue
    cb, cn = commands("base", base_tree, config), commands("new", new_tree, config)
    for rel in differing:
        eb, en = cb[str(rel)], cn[str(rel)]
        out = S / "kasm" / config
        out.mkdir(parents=True, exist_ok=True)
        sa, sb = out / (rel.name + ".base.s"), out / (rel.name + ".new.s")
        to_asm(eb, sa)
        to_asm(en, sb)
        verdict = subprocess.run([sys.executable, str(S / "asm_cmp.py"), str(sa), str(sb)],
                                 capture_output=True, text=True).stdout.strip()
        line = verdict.splitlines()[0] if verdict else "CMP-ERROR"
        if not verdict.startswith("same"):
            za, zb = out / (rel.name + ".base.O0.s"), out / (rel.name + ".new.O0.s")
            to_asm(eb, za, "-O0")
            to_asm(en, zb, "-O0")
            zero = subprocess.run([sys.executable, str(S / "asm_cmp0.py"), str(za), str(zb)],
                                  capture_output=True, text=True).stdout.strip()
            line += " | -O0: " + (zero.splitlines()[0] if zero else "CMP-ERROR")
        print(f"{config}: {rel} -> {line}", flush=True)
