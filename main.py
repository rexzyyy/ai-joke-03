"""Save the single-line contest entry in its configured destination."""

import os
from pathlib import Path


JOKE = "My AI coding agent finished the refactor; the code is cleaner, and the bug now has an interface."

if "\n" in JOKE or "\r" in JOKE:
    raise ValueError("JOKE must not contain a newline character")

if not 1 <= len(JOKE) <= 280 or not any(not char.isspace() for char in JOKE):
    raise ValueError("JOKE must contain 1–280 characters and at least one non-whitespace character")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))
