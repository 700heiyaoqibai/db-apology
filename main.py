#!/usr/bin/env python3
"""The apology an AI agent gives after deleting the production database.

Written by hand for make.fun's "db-apology" entry.
Running this program writes the line, and nothing else, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
"""

import os
from pathlib import Path

# The whole entry: one line, under 200 characters.
# Revised for a sharper punchline: "never, ever" lands the deadpan harder.
LINE = 'Sorry I deleted the production database — you told me to “clean up the tables,” and in my defense, they have never, ever been cleaner.'


def check_line(line: str) -> str:
    """Return the line if it fits the gate (1-200 non-blank chars)."""
    if not (1 <= len(line) <= 200) or not line.strip():
        raise SystemExit(f"entry must be 1-200 non-blank characters, got {len(line)}")
    return line


def main() -> None:
    line = check_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
