"""The Funniest Office Joke, Judged Head to Head — make.fun entry.

Builds a single-line office joke from three parts (setup, escalation,
punchline) joined with a single space, validates it against the contest
gate (one non-empty line, 1-200 characters), and writes it to
/output/entry.txt.

Structure: SETUP sets up the rename, ESCALATION raises the stakes with
Finance, PUNCHLINE lands the headcount twist. The entry is fully
deterministic: fixed literal text only, no randomness, no time, no
network access, and no file reads.
"""

import os
import sys

SETUP = "I renamed the Q3 layoff spreadsheet 'Project Sunrise' so HR would smile,"
ESCALATION = "and now Finance wants Sunrise's headcount for 2027."
PUNCHLINE = "Sunrise is three people, and I am two of them."


def build_entry():
    """Join the three joke parts into one single-line entry."""
    return " ".join([SETUP, ESCALATION, PUNCHLINE])


def main():
    """Validate the entry and write it to /output/entry.txt."""
    entry = build_entry()
    if not entry or "\n" in entry or "\r" in entry or not 1 <= len(entry) <= 200:
        print("error: entry must be a single non-empty line of 1-200 characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    # Output file: /output/entry.txt holds exactly one line, the entry itself.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
