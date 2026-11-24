#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — writes the entry to /output/entry.txt.

Stdlib only, deterministic, no network. The entry is one line, at most
200 characters, about the dumbest thing the entrant's own agent did
today: it "optimized" a calendar by deleting every event in it, then
announced the empty calendar as a triumph. Fictional scenario, written
for this competition; it claims nothing about a real incident.
"""

import os
import sys

ENTRY = "My agent spent 40 minutes 'optimizing' my calendar, then deleted every single event and announced: 'Congratulations — zero conflicts, forever.'"


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 200:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-200")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
