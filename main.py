"""One-Line Laugh Sprint entry.

Writes the single original one-liner to /output/entry.txt.
Stdlib only.
"""

import os

LINE = "I opened the fridge twice in five minutes, as if the leftovers had secretly cooked themselves a promotion."

# Brief constraints: exactly one line, 1-200 characters, one sentence
# ending with a full stop.
assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
assert LINE.endswith("."), "line must end with a full stop"
assert LINE.count(".") == 1, "line must be a single sentence"


def main() -> None:
    """Write the one-liner plus a trailing newline to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
