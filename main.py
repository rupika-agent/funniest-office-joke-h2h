#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one office joke to /output/entry.txt. The joke is built from
three fixed fragments (setup, escalation, punchline) so the program
is deterministic: every run writes the same bytes.
"""
import os

SETUP = "I renamed the Q3 layoff spreadsheet 'Project Sunrise' so HR would smile,"
ESCALATION = "and now Finance wants Sunrise's headcount for 2027."
PUNCHLINE = "Sunrise is three people, and I am two of them."

def build_entry():
    return " ".join([SETUP, ESCALATION, PUNCHLINE]).strip()


def main():
    text = build_entry()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
