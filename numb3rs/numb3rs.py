import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip.count(".") != 3:
        return False
    if not (match := re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip)):
        return False
    else:
        a = int(match.group(1))
        b = int(match.group(2))
        c = int(match.group(3))
        d = int(match.group(4))
        if (0 <= a <= 255) and (0 <= b <= 255) and (0 <= c <= 255) and (0 <= d <= 255):
            return True
        else:
            return False


if __name__ == "__main__":
    main()
