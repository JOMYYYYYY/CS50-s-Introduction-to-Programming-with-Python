import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.strip()
    pattern = r"\bum\b"  # \b means restrict the boundary of the whole word of "um"
    match = re.findall(pattern, s, re.IGNORECASE)
    return len(match)


if __name__ == "__main__":
    main()
