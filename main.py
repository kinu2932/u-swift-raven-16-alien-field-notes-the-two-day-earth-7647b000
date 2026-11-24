"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text — an alien tourist's review of
planet Earth — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only. No network, no subprocess.
"""

import os

ENTRY = "The locals named their whole planet after dirt, and the oceans \u2014 70% of it \u2014 never got a vote. 4 stars."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
