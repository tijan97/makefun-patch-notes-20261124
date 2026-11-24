"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line for a bug in real life / human biology to
$MAKEFUN_OUTPUT_DIR/entry.txt (default: out/entry.txt).
"""

import os

ENTRY = (
    "v2.0.1: fixed a bug where the brain replayed an embarrassing moment "
    "from 2014 every time the user tried to fall asleep."
)


def validate(text):
    """Enforce the brief's gate: 1-160 chars, single line, non-blank."""
    if not (1 <= len(text) <= 160):
        raise ValueError(f"entry must be 1-160 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Read back and confirm what was written is exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert validate(f.read()) == entry
    print(f"entry: {entry}")


if __name__ == "__main__":
    main()
