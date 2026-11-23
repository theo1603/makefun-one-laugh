"""The One-Line Laugh entry.

Writes one original funny line about everyday life to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.
"""

import os

LINE = (
    "I finally cleaned out my inbox, and the only email left was one I sent "
    "myself three years ago, reminding me to clean out my inbox."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
