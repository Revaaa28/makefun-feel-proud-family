#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one line, 160 characters) to /output/entry.txt,
per the competition gate: UTF-8 text of 1 to 280 characters, not only whitespace.

The line was chosen by manual ranking of ten candidates against the kit's judge
brief (criteria in the brief's own order) plus pairwise checks against strong
rival patterns. See ../candidates.md for the full ranking.
"""

import os

ENTRY = (
    "Judge, if you want to feel proud: my dad still introduces me as "
    "\u2018my son, the one who finally learned to do the dishes\u2019 "
    "\u2014 and he says it like I won the Olympics."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, must be 1-280"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip verification: refuse to exit 0 unless what landed on disk
    # is byte-exact to the chosen line, so a silent short write can never
    # ship a losing entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the chosen line"
    assert len(written.encode("utf-8")) == 166, "entry.txt must be 166 bytes (160 chars)"


if __name__ == "__main__":
    main()
