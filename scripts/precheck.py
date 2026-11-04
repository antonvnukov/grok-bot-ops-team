#!/usr/bin/env python3
"""Wake a bot only when its input changed. Exit 0 = wake, 1 = skip.
Usage: precheck.py <input-file> <state-file>    Self-test: precheck.py --self-test"""
import hashlib, pathlib, sys, tempfile

def changed(inp, state):
    h = hashlib.sha256(pathlib.Path(inp).read_bytes()).hexdigest()
    s = pathlib.Path(state)
    if s.exists() and s.read_text() == h:
        return False
    s.write_text(h)
    return True

def self_test():
    d = pathlib.Path(tempfile.mkdtemp())
    (d / "q").write_text("a")
    assert changed(d / "q", d / "s") is True
    assert changed(d / "q", d / "s") is False
    (d / "q").write_text("b")
    assert changed(d / "q", d / "s") is True
    print("self-test ok")

if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test(); sys.exit(0)
    sys.exit(0 if changed(sys.argv[1], sys.argv[2]) else 1)
