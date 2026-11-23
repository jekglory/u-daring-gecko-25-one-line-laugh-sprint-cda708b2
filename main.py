#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line (<=200 chars) to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = (
    "I bought a standing desk to be healthier. "
    "Now I sit on a taller chair and look down on everyone "
    "\u2014 literally and morally."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    assert len(LINE) <= 200, "line exceeds 200 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-char line to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
