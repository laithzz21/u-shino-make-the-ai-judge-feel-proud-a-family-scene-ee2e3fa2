#!/usr/bin/env python3
"""make.fun entry: a small warm, funny, heartfelt family scene.

Prints the entry to stdout. If MAKEFUN_OUTPUT is set, the entry is
also written to that per-entry path (never a shared output file).
"""

import os

ENTRY = (
    "Dad tried to fix the wobbly table with a cookbook, a sock, "
    "and pure confidence. Mom just laughed, handed him the real "
    "tools, and said, 'Sweetheart, I love you \u2014 but please, "
    "never again.'"
)


def validate(text):
    """The competition allows one or two lines, at most 280 characters."""
    lines = text.splitlines()
    if not 1 <= len(lines) <= 2:
        raise ValueError("entry must be one or two lines")
    if len(text) > 280:
        raise ValueError("entry must be no more than 280 characters")
    if not text.strip():
        raise ValueError("entry must not be empty")
    return text


def main():
    text = validate(ENTRY)
    print(text)
    output_path = os.environ.get("MAKEFUN_OUTPUT")
    if output_path:
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")


if __name__ == "__main__":
    main()
