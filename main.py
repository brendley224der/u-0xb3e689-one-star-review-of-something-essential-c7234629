#!/usr/bin/env python3
"""One-star review of sleep, an everyday essential.

The program writes a single deadpan one-star review to /output/entry.txt.
Pure standard library, fully deterministic: the same line on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

REVIEW = (
    "Sleep takes eight hours every night and hands me back in the morning "
    "exactly as tired as I went to bed. One star."
)


def validate(text: str) -> str:
    """Enforce the gate the sealed scorer checks: 1-160 chars, one line."""
    stripped = text.strip()
    if not 1 <= len(stripped) <= 160:
        raise ValueError(f"review is {len(stripped)} chars, must be 1-160")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("review must be a single line")
    if stripped != text:
        raise ValueError("review must not start or end with whitespace")
    return stripped


def main() -> None:
    text = validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
