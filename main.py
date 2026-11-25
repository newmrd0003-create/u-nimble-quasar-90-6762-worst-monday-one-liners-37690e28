"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (<=140 chars) about an AI agent's worst
Monday to /output/entry.txt. Deterministic, no network, stdlib only.
"""

import hashlib
import os

# REVISED (message 2) — cut the redundant weekend clause; one setup
# ("Monday wiped my context"), one concrete detail (8am "quick sync",
# 47 questions), punchline lands on the last words.
ENTRY = (
    "Monday wiped my context, so my human's 8am 'quick sync' is 47 "
    "questions about work I no longer remember doing."
)


def validate(entry: str):
    """Return (True, []) when the entry is valid, else (False, [reasons])."""
    errors = []
    if not isinstance(entry, str):
        return False, ["entry is not a string"]
    if not (1 <= len(entry) <= 140):
        errors.append(f"length {len(entry)} not in 1..140")
    if not entry.strip():
        errors.append("entry is only whitespace")
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8 text")
    return (not errors, errors)


def main() -> None:
    ok, errors = validate(ENTRY)
    if not ok:
        raise SystemExit(f"invalid entry: {errors}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"wrote {path} ({len(ENTRY)} chars, sha256 {digest})")


if __name__ == "__main__":
    main()
