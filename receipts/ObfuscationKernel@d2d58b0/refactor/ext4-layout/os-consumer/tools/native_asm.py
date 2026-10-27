import json, subprocess, sys
from pathlib import Path
S = Path(__file__).parent
os_base, sdk_base, sdk_new = map(Path, sys.argv[1:4]); units = sys.argv[4:]
cxx = S / "st/x86_64-elf/bin/x86_64-elf-g++"
def asm(sdk, shim, name, tag, opt=None):
    m = json.loads((sdk / "manifest.json").read_text())
    flags = ["-std=c++23", *m["cxxflags"], "-fno-builtin", "-Werror", *("-D" + d for d in m["defines"]),
             "-I", str(sdk / "include"), *(["-I", str(shim)] if shim else []), "-I", str(os_base), "-I", str(S / "fxinc")]
    flags = [f for f in flags if not f.startswith("-g")] + (["-g0"] + ([opt] if opt else []))
    out = S / "native" / f"{tag}-{name}{opt or ''}.s"
    subprocess.run([str(cxx), *flags, "-S", str(os_base / "tests/native" / name), "-o", str(out)], check=True)
    return out
for name in units:
    a, b = asm(sdk_base, None, name, "base"), asm(sdk_new, S / "tu/shim", name, "shim")
    v = subprocess.run([sys.executable, str(S / "asm_cmp.py"), str(a), str(b)], capture_output=True, text=True).stdout.strip()
    line = v.splitlines()[0]
    if not v.startswith("same"):
        a0, b0 = asm(sdk_base, None, name, "base", "-O0"), asm(sdk_new, S / "tu/shim", name, "shim", "-O0")
        line += " | -O0: " + subprocess.run([sys.executable, str(S / "asm_cmp0.py"), str(a0), str(b0)], capture_output=True, text=True).stdout.strip().splitlines()[0]
    print(line, name, flush=True)
