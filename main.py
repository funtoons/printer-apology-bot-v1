"""Printer Apology entry for make.fun.

Writes one line (1-120 characters) to /output/entry.txt: an apology
note from an office printer to the people who keep jamming it, feeding
it cheap paper and swearing at it.

Deterministic and offline: standard library only, no randomness, no
network, no timestamps, no paths in the output.
"""

import os

ENTRY = (
    "Sorry I jammed on page 47 of 48. "
    "Your cheap paper tasted like cardboard, "
    "so I kept the last page for myself."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Read-back gate: what the grader reads must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written entry does not match ENTRY"


if __name__ == "__main__":
    main()
