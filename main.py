#!/usr/bin/env python3
"""The One-Line Laugh — write one funny line to the entry file.

Stdlib only, no network, no wall clock. The line is a single sentence
(117 chars) that lands its surprise at the very end: the tracker that
counts calories burned is the same one you were reading while eating.
"""

import os
import sys
import tempfile

LINE = (
    "My fitness tracker says I burned 400 calories today, "
    "which is exactly how many I ate while reading that notification."
)


def validate(line: str) -> str:
    """Check the line against the competition rules; return an error or ''."""
    if line != line.strip():
        return "line has leading or trailing whitespace"
    if any(ord(c) < 0x20 for c in line):
        return "line contains a control character"
    if not line.endswith("."):
        return "line must be a single sentence"
    if line.count(".") != 1:
        return "line must be exactly one sentence"
    if len(line) > 200:
        return "line exceeds 200 characters"
    return ""


def write_entry(out_dir: str) -> None:
    """Atomically write entry.txt, then verify it by reading it back."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    fd, tmp_path = tempfile.mkstemp(
        dir=out_dir, prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE + "\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, out_path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    with open(out_path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE + "\n":
        raise RuntimeError("entry.txt failed read-back verification")


def main() -> int:
    error = validate(LINE)
    if error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        write_entry(out_dir)
    except OSError as exc:
        print(f"error: cannot write entry: {exc}", file=sys.stderr)
        return 1
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
