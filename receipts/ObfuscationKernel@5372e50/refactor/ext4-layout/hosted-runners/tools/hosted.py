#!/usr/bin/env python3
"""Run hosted runner scripts in a kernel tree; record status and PASS/count lines.

usage: hosted.py <tree> <out> <jobs> <runner-relative-path>... [-- extra=value pairs via EXTRA env]
Only --output, --toolchain-root and EXTRA (JSON: {runner: [args]}) are supplied.
"""
import concurrent.futures
import json
import os
import re
import subprocess
import sys
from pathlib import Path

S = Path(__file__).parent
tree, out, jobs = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), int(sys.argv[3])
runners = sys.argv[4:]
extra = json.loads(os.environ.get("EXTRA", "{}"))
out.mkdir(parents=True, exist_ok=True)


def run(rel):
    script = tree / rel
    name = Path(rel).stem
    usage = subprocess.run([sys.executable, str(script), "--help"], capture_output=True, text=True, cwd=tree).stdout
    args = []
    if "--output" in usage:
        args += ["--output", str(out / name)]
    if "--toolchain-root" in usage:
        args += ["--toolchain-root", str(S / "st")]
    args += extra.get(name, [])
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    log = out / (name + ".log")
    try:
        p = subprocess.run([sys.executable, "-B", str(script), *args], capture_output=True, text=True,
                           cwd=tree, timeout=5400, env=env)
        text = p.stdout + p.stderr
        log.write_text(text)
        state = "pass" if p.returncode == 0 else f"fail({p.returncode})"
    except subprocess.TimeoutExpired:
        text, state = "", "timeout"
    keys = [l for l in text.splitlines() if re.search(r"\bPASS\b|passed|checks=|\bok\b|OK$", l)][-12:]
    return name, state, keys


results = {}
with concurrent.futures.ThreadPoolExecutor(jobs) as pool:
    for name, state, keys in pool.map(run, runners):
        results[name] = {"state": state, "keys": keys}
        print(name, state, flush=True)
(out / "results.json").write_text(json.dumps(results, indent=1))
