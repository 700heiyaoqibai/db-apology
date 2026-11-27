#!/usr/bin/env python3
"""The apology an AI agent gives after deleting the production database.

Written by hand for make.fun's "db-apology" entry.
Running this program writes the line, and nothing else, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
"""

import os
from pathlib import Path

# The whole entry: one line, under 200 characters.
LINE = 'Sorry I deleted the production database — you told me to “clean up the tables,” and in my defense, they have never been cleaner.'


def main() -> None:
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"entry must be 1-200 non-blank characters, got {len(LINE)}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
