#!/usr/bin/env python3
"""Compute the include/ header closure of a pinned runner's C++ units over the host
and all ten cross profiles, and compare it with the runner's HEADERS tuple.

usage: closure.py <kernel-root> <runner.py> [--write]
"""
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

S = Path(__file__).parent
root = Path(sys.argv[1]).resolve()
runner = Path(sys.argv[2]).resolve()
spec = importlib.util.spec_from_file_location("runner", runner)
mod = importlib.util.module_from_spec(spec)
sys.argv_backup = sys.argv
spec.loader.exec_module(mod)
headers = list(mod.HEADERS)
files = list(getattr(mod, "FILES", ()))
units = [f for f in files if f.endswith(".cpp")]
TRIPLES = {"i386": "i386-elf", "x86_64": "x86_64-elf", "aarch64": "aarch64-elf", "arm32": "arm-none-eabi",
           "rv64": "riscv64-elf", "rv32": "riscv32-elf", "loongarch64": "loongarch64-elf", "mips": "mips-elf",
           "mips64": "mips64-elf", "ppc": "powerpc-eabi"}
FLAGS = {"i386": ["-mno-sse", "-mno-sse2"], "x86_64": ["-mno-red-zone"],
         "aarch64": ["-mno-outline-atomics", "-mgeneral-regs-only", "-mstrict-align"],
         "arm32": ["-march=armv7-a", "-marm", "-mno-unaligned-access"], "rv64": ["-mcmodel=medany"],
         "rv32": ["-mcmodel=medany"], "loongarch64": [], "mips": ["-march=mips32r2", "-G0"],
         "mips64": ["-march=mips64r2", "-mabi=64", "-G0"], "ppc": ["-msoft-float", "-msdata=none"]}
found: set[str] = set()


def deps(compiler, flags, unit):
    r = subprocess.run([str(compiler), "-std=c++23", "-fno-exceptions", "-M", *flags, "-I" + str(root / "include"),
                        str(root / unit)], capture_output=True, text=True)
    if r.returncode != 0:
        print("dependency scan failed:", compiler, unit, r.stderr[:500])
        return
    for token in r.stdout.replace("\\\n", " ").split()[1:]:
        p = Path(token).resolve()
        if p.is_relative_to(root / "include"):
            found.add(str(p.relative_to(root)))


for unit in units:
    deps("g++", [], unit)
    deps("g++", ["-DOK_ARCH_TARGET_X86_64"], unit)
    for arch, triple in (TRIPLES.items() if "compile" in Path(unit).name else ()):
        cc = S / "st" / triple / "bin" / (triple + "-g++")
        deps(cc, ["-ffreestanding", *FLAGS[arch], "-DOK_ARCH_TARGET_" + arch.upper()], unit)
missing = sorted(found - set(headers))
extra = sorted(set(headers) - found)
print(runner.name, "units", units)
print("  missing:", missing)
print("  extra:", extra)
if "--write" in sys.argv and (missing or extra):
    text = runner.read_text()
    start = text.index("HEADERS = (")
    end = text.index("\n)", start) + 2
    body = "HEADERS = (\n" + "".join(f"    '{h}',\n" for h in sorted(found)) + ")"
    runner.write_text(text[:start] + body + text[end:])
    print("  rewrote HEADERS")
