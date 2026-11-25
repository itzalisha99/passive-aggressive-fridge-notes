#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one passive-aggressive note a smart fridge leaves for its owner
to /output/entry.txt. The note is a single dry, petty line: the fridge
kept an expired yogurt out of sheer commitment, unlike its owner.
"""

import os

ENTRY = "The yogurt expired on Tuesday. I kept it anyway, because unlike you, I commit to things."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only white space,
    and a single line. Raise ValueError on anything the gate would refuse."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file is byte-identical to the entry.
    with open("/output/entry.txt", "rb") as f:
        if f.read() != ENTRY.encode("utf-8"):
            raise ValueError("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
