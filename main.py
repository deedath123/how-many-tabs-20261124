"""Write the make.fun 'How Many Tabs Do You Have Open?' entry.

The entry is a single number in digits and nothing else: 137, my honest
count of open browser tabs right now. This program writes exactly those
3 characters (3 bytes, digits only, no trailing newline) to entry.txt
in the output directory named by MAKEFUN_OUTPUT_DIR (default /output).

End-to-end check: verified by running — the written entry.txt is
exactly 3 characters, 3 bytes, digits only, with no trailing newline
(content "137", bytes 31 33 37).
"""

import os
from pathlib import Path

ENTRY_TEXT = "137"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
