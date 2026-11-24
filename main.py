#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt (stdlib only, deterministic).
"""

import os

# FINAL entry (v4, tightened to fit 240 chars):
# - kept: morning sock interview, emotional compatibility, vivid mismatch
# - cut: "every"->"each", "just", "dreams of"->"wants", "again"
#   (14 chars trimmed, nothing else lost)
ENTRY = (
    "SockSync is an AI app that interviews your socks each morning and "
    "pairs them by emotional compatibility, so busy professionals never "
    "suffer the quiet heartbreak of a left sock that wants adventure "
    "and a right sock that wants to stay home."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
