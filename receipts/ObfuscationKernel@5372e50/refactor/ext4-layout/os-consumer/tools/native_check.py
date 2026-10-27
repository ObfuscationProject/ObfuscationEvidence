#!/usr/bin/env python3
"""Compile every OS tests/native unit that reaches an ext4 header against an SDK,
for the baseline OS + baseline SDK and the paired OS + new SDK, and compare.

usage: native_check.py <os-base> <sdk-base> <os-new> <sdk-new> <out>
"""
import json
import re
import subprocess
import sys
from pathlib import Path

S = Path(__file__).parent
os_base, sdk_base, os_new, sdk_new, out = map(Path, sys.argv[1:6])
cxx = S / "st/x86_64-elf/bin/x86_64-elf-g++"
units = sorted(p.name for p in (os_new / "tests/native").glob("*.cpp")
               if re.search(r"ok/fs/ext4/", p.read_text(errors="replace")))
out.mkdir(parents=True, exist_ok=True)


def compile_unit(tree, sdk, name, tag, shim=None):
    manifest = json.loads((sdk / "manifest.json").read_text())
    flags = ["-std=c++23", *manifest["cxxflags"], "-fno-builtin", "-Werror", *("-D" + d for d in manifest["defines"]),
             "-I", str(sdk / "include"), *(["-I", str(shim)] if shim else []), "-I", str(tree), "-I", str(S / "fxinc")]
    obj = out / f"{tag}-{name}.o"
    r = subprocess.run([str(cxx), *flags, "-c", str(tree / "tests/native" / name), "-o", str(obj)],
                       capture_output=True, text=True)
    errors = sorted({re.sub(r"^[^ ]*:\d+:\d+: ", "", l) for l in r.stderr.splitlines() if "error:" in l})
    return r.returncode, obj, errors


for name in units:
    rb, ob, eb = compile_unit(os_base, sdk_base, name, "base")
    rn, on, en = compile_unit(os_base, sdk_new, name, "shim", S / "tu/shim")
    rp, _, ep = compile_unit(os_new, sdk_new, name, "new")
    print("new-source", "compiles" if rp == 0 else "FAILS " + (ep[0][:160] if ep else ""), name)
    if rb == 0 and rn == 0:
        a = subprocess.run([str(S / "st/x86_64-elf/bin/x86_64-elf-objdump"), "-d", "--no-show-raw-insn", str(ob)],
                           capture_output=True, text=True).stdout.splitlines()[2:]
        b = subprocess.run([str(S / "st/x86_64-elf/bin/x86_64-elf-objdump"), "-d", "--no-show-raw-insn", str(on)],
                           capture_output=True, text=True).stdout.splitlines()[2:]
        state = "identical-object" if ob.read_bytes() == on.read_bytes() else (
            "same-disassembly" if a == b else "compiled-both-code-differs")
    elif rb != 0 and rn != 0:
        state = "fails-both-same-errors" if eb == en else "fails-both-DIFFERENT-errors"
    else:
        state = f"BASE-{'ok' if rb == 0 else 'fail'}-NEW-{'ok' if rn == 0 else 'fail'}"
        if rn != 0:
            state += " :: " + (en[0][:200] if en else "")
    print(state, name, flush=True)
