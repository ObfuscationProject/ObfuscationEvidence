#!/usr/bin/env python3
"""For every TU the object oracle could not prove identical, compile both sides to
assembly and compare per symbol with asm_cmp.py.

usage: asm_oracle.py <baseline-tree> <new-tree> <tu-out> <jobs>
"""
import concurrent.futures
import json
import subprocess
import sys
from pathlib import Path

base, new, out, jobs = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), int(sys.argv[4])
opt = sys.argv[5] if len(sys.argv) > 5 else "-O2"
only = Path(sys.argv[6]).read_text().split() if len(sys.argv) > 6 else None
here = Path(__file__).parent
shim = out / "shim"
results = json.loads((out / "results.json").read_text())
FLAGS = ["-std=c++23", opt, "-fno-exceptions", "-frtti", "-w", "-DOK_ARCH_TARGET_X86_64"]
todo = [rel for rel, (state, _) in results.items()
        if state in ("CODE-DIFFERS", "same-code", "ACCESS-CONTROL-DIFFERS") and (only is None or rel in only)]


def one(rel):
    unit = base / rel
    tag = rel.replace("/", "__")
    files = {}
    for side, incs in (("base", [base / "include"]), ("new", [new / "include", shim])):
        asm = out / ("asm" + opt) / side / (tag + ".s")
        asm.parent.mkdir(parents=True, exist_ok=True)
        for attempt in ([], ["-fno-access-control"]):
            r = subprocess.run(["g++", *FLAGS, *attempt, *("-I" + str(i) for i in incs), "-I" + str(base / "tests/host"),
                                "-S", str(unit), "-o", str(asm)], capture_output=True, text=True, cwd=unit.parent)
            if r.returncode == 0:
                break
        if r.returncode != 0:
            return rel, "compile-fail " + side
        files[side] = (asm, attempt)
    cmp = subprocess.run([sys.executable, str(here / "asm_cmp.py"), str(files["base"][0]), str(files["new"][0])],
                         capture_output=True, text=True)
    flags = "" if files["base"][1] == files["new"][1] else f" (access flags base={files['base'][1]} new={files['new'][1]})"
    return rel, (cmp.stdout.strip() or "CMP-ERROR " + cmp.stderr.strip()[-300:]) + flags


summary = {}
with concurrent.futures.ThreadPoolExecutor(jobs) as pool:
    for rel, verdict in pool.map(one, todo):
        print(verdict.split("\n")[0][:60].ljust(60), rel, flush=True)
        if not verdict.startswith("same"):
            print(verdict)
        key = verdict.split()[0]
        summary[key] = summary.get(key, 0) + 1
print(json.dumps(summary))
