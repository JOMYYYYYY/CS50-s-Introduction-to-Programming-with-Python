import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src="([^"]+)"', s)
    if match:
        url = match.group(1)
        if "https://www.youtube.com/embed/" in url:
            url = url.replace("https://www.youtube.com/embed/", "https://youtu.be/")
            return url
        elif "http://www.youtube.com/embed/" in url:
            url = url.replace("http://www.youtube.com/embed/", "https://youtu.be/")
            return url
        elif "https://youtube.com/embed/" in url:
            url = url.replace("https://youtube.com/embed/", "https://youtu.be/")
            return url
        elif "http://youtube.com/embed/" in url:
            url = url.replace("http://youtube.com/embed/", "https://youtu.be/")
            return url

if __name__ == "__main__":
    main()