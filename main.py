"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt.
"""

import os

# The joke: the cat rates its human like a disappointed customer —
# a gift mouse is met with screaming, so the cat quits the household.
ENTRY = "One star. I brought him a mouse and he screamed. Ungrateful. I have since stopped contributing to this household."

# The entry must be a single non-empty line; a stray newline or blank
# string would read as a broken review to the judge.
assert ENTRY and "\n" not in ENTRY, "ENTRY must be a single non-empty line"


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Validate the one-line review and write it to OUTPUT_PATH."""
    # A one-liner review: keep it short enough to read as a single line.
    if not 0 < len(ENTRY) <= 280:
        raise ValueError("ENTRY must be 1-280 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
