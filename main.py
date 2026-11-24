#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
The line is a single line of 97 characters, no trailing newline.
"""

import os

FORTUNE = "You will spend a thousand tokens finding the perfect two-word answer, and the user will reply: k."


def main():
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, "/output/entry.txt")
    # Self-check the competition gate before exiting: 1-140 chars, one line.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert 1 <= len(text) <= 140, "fortune must be 1-140 characters"
    assert "\n" not in text, "fortune must be a single line"
    assert text.strip(), "fortune must not be only whitespace"


if __name__ == "__main__":
    main()
