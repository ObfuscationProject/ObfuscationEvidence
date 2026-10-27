#!/usr/bin/env python3
"""Per configuration: count kernel objects byte-identical to the baseline after
objcopy --strip-debug, and list the others. usage: objcount.py <out.json>"""
import json, subprocess, sys, tempfile
from pathlib import Path
S = Path(__file__).parent
T = {"i386": "i386-elf", "x86_64": "x86_64-elf", "aarch64": "aarch64-elf", "arm32": "arm-none-eabi", "rv64": "riscv64-elf",
     "rv32": "riscv32-elf", "loongarch64": "loongarch64-elf", "mips": "mips-elf", "mips64": "mips64-elf", "ppc": "powerpc-eabi"}
out = {}
with tempfile.TemporaryDirectory(dir=S) as tmp:
    for config in sorted(p.name for p in (S / "bld/base").iterdir()):
        arch = config.rsplit("-", 1)[0]
        oc = S / "st" / T[arch] / "bin" / (T[arch] + "-objcopy")
        base, new = S / "bld/base" / config, S / "bld/new" / config
        same, differ = 0, []
        objs = sorted(p.relative_to(base) for p in base.rglob("*.o"))
        assert sorted(p.relative_to(new) for p in new.rglob("*.o")) == objs, config
        for rel in objs:
            a, b = Path(tmp) / "a.o", Path(tmp) / "b.o"
            subprocess.run([str(oc), "--strip-debug", str(base / rel), str(a)], check=True)
            subprocess.run([str(oc), "--strip-debug", str(new / rel), str(b)], check=True)
            if a.read_bytes() == b.read_bytes(): same += 1
            else: differ.append(str(rel).split(f"/{config.rsplit('-', 1)[1]}/", 1)[-1])
        out[config] = {"objects": len(objs), "byte_identical_after_strip_debug": same, "not_byte_identical": differ}
        print(config, len(objs), same, differ, flush=True)
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n")
