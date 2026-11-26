#!/usr/bin/env python3
"""Texts From Your Future Self — one funny text from your future self.

Writes exactly one line (<=140 chars) to /output/entry.txt.
Deterministic, no network, no randomness: the same line every run.
"""

import os

LINE = (
    "It's you from 2041. The 'temporary' tattoo lasted 40 years, "
    "the marriage lasted 6 months, and the houseplant outlived us both. "
    "Water it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Clean only the contents of the output folder, never the folder itself.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, "entry must be 1-140 chars, got %d" % len(line)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
