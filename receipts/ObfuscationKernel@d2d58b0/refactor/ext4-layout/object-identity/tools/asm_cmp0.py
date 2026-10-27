#!/usr/bin/env python3
"""-O0 comparison on top of asm_cmp: ctor/dtor C1/C2 and D1/D2 variants are one
symbol; one-sided data objects that no compared function references are listed
separately as unreferenced instantiations."""
import importlib.util, re, sys
spec = importlib.util.spec_from_file_location("a", "<scratch>/asm_cmp.py")
src = open(spec.origin).read().split("\na, pa = parse")[0]
ns = {}; exec(src, ns)
CTOR = re.compile(r"(?<=[0-9A-Za-z_])([CD])[12](?=[EI])")
def norm(path):
    syms, _ = ns["parse"](path)
    kinds = {}
    for line in open(path):
        m = re.match(r"^\s*\.type\s+([^,]+),\s*@(\w+)", line)
        if m: kinds[m.group(1)] = m.group(2)
    out = {}
    for k, bodies in syms.items():
        key = CTOR.sub(r"\1x", k)
        body = [CTOR.sub(r"\1x", b) for b in bodies]
        out.setdefault(key, set()).update(body)
    kinds = {CTOR.sub(r"\1x", k): v for k, v in kinds.items()}
    return out, kinds
a, ka = norm(sys.argv[1]); b, kb = norm(sys.argv[2])
text_a = "\n".join(x for v in a.values() for x in v); text_b = "\n".join(x for v in b.values() for x in v)
diff, unref = [], []
for k in sorted(set(a) | set(b)):
    if a.get(k) == b.get(k): continue
    one_sided = (k in a) != (k in b)
    kind = ka.get(k) or kb.get(k)
    if one_sided and kind == "object" and k not in text_a and k not in text_b:
        unref.append(k); continue
    diff.append(k)
print(("same" if not diff else f"DIFF {len(diff)}") + f" unreferenced-one-sided-objects={len(unref)} symbols={len(a)}")
for k in diff[:10]: print("  ", k, "only-a" if k not in b else "only-b" if k not in a else "")
