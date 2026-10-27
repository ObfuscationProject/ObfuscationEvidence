import json, re, sys
from pathlib import Path
base, new = Path(sys.argv[1]), Path(sys.argv[2])
SKIP = re.compile(r"sha256|digest|path|argv|cwd|seconds|source|files|commands|kernel_root|output|log|tool|compiler|time|duration", re.I)
def strip(v, key=""):
    if isinstance(v, dict): return {k: strip(x, k) for k, x in v.items() if not SKIP.search(k)}
    if isinstance(v, list): return [strip(x) for x in v]
    if isinstance(v, str) and ("/" in v and ("scratchpad" in v or "worktrees" in v or "/tmp/" in v)): return "<path>"
    return v
for r in sorted(base.glob("*/result.json")):
    n = new / r.parent.name / "result.json"
    if not n.exists(): print("missing-new", r.parent.name); continue
    a, b = strip(json.loads(r.read_text())), strip(json.loads(n.read_text()))
    print(("same-result " if a == b else "DIFFERENT-result ") + r.parent.name)
    if a != b:
        for k in sorted(set(a) | set(b)):
            if a.get(k) != b.get(k): print("   ", k, str(a.get(k))[:150], "|", str(b.get(k))[:150])
