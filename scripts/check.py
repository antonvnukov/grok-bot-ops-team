#!/usr/bin/env python3
"""Repo gate. Run: python3 scripts/check.py   Self-test: python3 scripts/check.py --self-test
Checks: every tasks/*/log.jsonl line has all keys and a valid receipt; BLOCKED and
HUMAN_HOLD carry [ask: <class>]; every bot in a log has a block in bots/<slug>/block.md."""
import json, re, sys, pathlib, tempfile

KEYS = {"ts", "bot", "receipt", "task", "note"}
RECEIPTS = {"CLAIMED", "DONE", "BLOCKED", "HUMAN_HOLD", "FAILED", "FOLLOW_UP"}
STOP = re.compile(r"\[ask: (send|money|delete|credential|brand|fact)\]")

def check_line(line, slugs):
    """Return an error string or None for one log line."""
    try:
        d = json.loads(line)
    except ValueError:
        return "not JSON"
    if not isinstance(d, dict) or not KEYS <= d.keys():
        return "missing keys"
    if d["receipt"] not in RECEIPTS:
        return f"bad receipt {d['receipt']}"
    if d["receipt"] in {"BLOCKED", "HUMAN_HOLD"} and not STOP.search(d["note"]):
        return "stop without [ask: class]"
    if d["bot"].lower() not in slugs:
        return f"no block for bot {d['bot']}"
    return None

def run(root):
    root = pathlib.Path(root)
    slugs = {p.parent.name for p in root.glob("bots/*/block.md") if p.parent.name != "_template"}
    logs = list(root.glob("tasks/*/log.jsonl"))
    errs = []
    for f in logs:
        for n, line in enumerate(f.read_text().splitlines(), 1):
            if line.strip() and (e := check_line(line, slugs)):
                errs.append(f"{f}:{n}: {e}")
    return errs, len(logs)

def self_test():
    good = '{"ts":"t","bot":"Chief","receipt":"DONE","task":"x","note":"ok"}'
    bad = '{"ts":"t","bot":"Chief","receipt":"BLOCKED","task":"x","note":"need yes"}'
    s = {"chief"}
    assert check_line(good, s) is None
    assert check_line(bad, s) == "stop without [ask: class]"
    assert check_line('{"bot":"Chief"}', s) == "missing keys"
    assert check_line(good.replace("Chief", "Nobody"), s).startswith("no block")
    print("self-test ok")

if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test(); sys.exit(0)
    errs, n = run(pathlib.Path(__file__).resolve().parent.parent)
    print("\n".join(errs) or f"ok ({n} logs)")
    sys.exit(1 if errs else 0)
