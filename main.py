#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (the sealed gate requires UTF-8 text of 1-400
characters, not only whitespace). When /output is not writable
(local runs), falls back to ./output/entry.txt next to this file.
"""

import os
import sys

RANT = (
    "My smoke alarm has one job, and it does it exclusively at 3 a.m. "
    "Never at noon, never while I'm awake holding a ladder \u2014 always "
    "at 3 a.m., one smug chirp, then silence, like it's checking I'm "
    "still breathing just to ruin my sleep. Four new batteries. "
    "The house isn't on fire. I am."
)


def main() -> int:
    text = RANT.strip()
    if not 1 <= len(text) <= 400:
        print(f"rant is {len(text)} characters, must be 1-400", file=sys.stderr)
        return 1
    # Primary target: the harness path the sealed gate reads.
    written = []
    for out_dir in ("/output", os.path.join(os.path.dirname(__file__), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            written.append(path)
        except OSError:
            continue
    if not written:
        print("could not write entry.txt anywhere", file=sys.stderr)
        return 1
    # Self-check: re-read the primary copy and confirm the gate rules.
    with open(written[0], encoding="utf-8") as f:
        check = f.read()
    assert 1 <= len(check) <= 400 and check.strip(), "gate check failed"
    print(f"wrote {len(text)} characters to {', '.join(written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
