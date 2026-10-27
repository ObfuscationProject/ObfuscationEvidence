#!/usr/bin/env python3
"""Compare two GCC assembly files per symbol, independent of emission order.

Local labels are renumbered per symbol in order of appearance; .LC constants are
replaced by a digest of their contents (following .set aliases). Prints 'same'
or the differing symbols.
usage: asm_cmp.py a.s b.s
"""
import hashlib
import re
import sys
from collections import Counter

LOCAL = re.compile(r"(?:\.L|\$L)(?!C\d)[A-Za-z_]*\d+")
CONST = re.compile(r"\.LC\d+|\$LC\d+|CSWTCH\.\d+")
LABEL = re.compile(r"^([A-Za-z_.$][\w.$]*):$")
OBJECT_END = re.compile(r"^\s*\.(section|text|data|bss|set|globl|weak|hidden|protected|internal|type|align|p2align|balign|size|local|comm|ident)\b")


def parse(path):
    lines = open(path).read().splitlines()
    kinds = {}
    for line in lines:
        m = re.match(r"^\s*\.type\s+([^,]+),\s*@(\w+)", line)
        if m:
            kinds[m.group(1)] = m.group(2)
    consts, aliases, current = {}, {}, None
    for line in lines:
        m = re.match(r"^\s*\.set\s+(\.LC\d+|\$LC\d+|CSWTCH\.\d+),\s*(\.LC\d+|\$LC\d+|CSWTCH\.\d+)([+-]\d+)?$", line)
        if m:
            aliases[m.group(1)] = (m.group(2), m.group(3) or "")
            current = None
            continue
        m = LABEL.match(line)
        if m:
            current = m.group(1) if CONST.fullmatch(m.group(1)) else None
            if current:
                consts[current] = []
            continue
        if current:
            if OBJECT_END.match(line):
                current = None
            else:
                consts[current].append(line.strip())
    digest = {k: "LC_" + hashlib.sha1("\n".join(v).encode()).hexdigest()[:12] for k, v in consts.items()}

    def resolve(name, depth=0):
        if name in digest:
            return digest[name]
        if name in aliases and depth < 8:
            base, offset = aliases[name]
            return resolve(base, depth + 1) + offset
        return name

    symbols, name, body, kind = {}, None, [], None

    def close():
        nonlocal name, body
        if name:
            symbols.setdefault(name, []).append(body)
        name, body = None, []

    for line in lines:
        m = LABEL.match(line)
        if m and not m.group(1).startswith((".L", "$L")) and not CONST.fullmatch(m.group(1)):
            close()
            name, kind = m.group(1), kinds.get(m.group(1), "unknown")
            continue
        if name is None:
            continue
        s = line.strip()
        if kind != "function" and (LABEL.match(line) or OBJECT_END.match(line)):
            close()
            continue
        if s.startswith((".file", ".ident", ".loc", ".cfi_sections")):
            continue
        body.append(s)
        if kind == "function" and re.match(rf"^\.size\s+{re.escape(name)},", s):
            close()
    close()
    out = {}
    for sym, bodies in symbols.items():
        norm = []
        for b in bodies:
            labels = {}
            text = "\n".join(b)
            text = CONST.sub(lambda m: resolve(m.group(0)), text)
            text = LOCAL.sub(lambda m: labels.setdefault(m.group(0), f".LX{len(labels)}"), text)
            norm.append(text)
        out[sym] = sorted(norm)
    pool = Counter(tuple(v) for v in consts.values())
    return out, pool


a, pa = parse(sys.argv[1])
b, pb = parse(sys.argv[2])
diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
if not diff and pa == pb:
    print("same", len(a))
else:
    print("DIFF", len(diff), "pool-equal" if pa == pb else "pool-differs")
    for k in diff[:15]:
        print("  ", k, "only-a" if k not in b else "only-b" if k not in a else "")
