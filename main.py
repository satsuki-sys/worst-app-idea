#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt (stdlib only, deterministic).
"""

import os

# FINAL entry (v2, revised against the judge brief):
# - sharper absurd logic: "emotional compatibility" between socks
# - deadpan founder confidence: "AI app", "quiet heartbreak"
# - one sentence, one idea, uses more of the 240 characters
ENTRY = (
    "SockSync is an AI app that pairs your left sock with your right sock "
    "by emotional compatibility, so busy professionals never again suffer "
    "the quiet heartbreak of wearing two socks that feel differently "
    "about the day."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
