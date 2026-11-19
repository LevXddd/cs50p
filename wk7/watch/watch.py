import re
import sys

# let's imagine that our parse is: r'src="https?://(www\.)?youtube\.com/embed/([\w-]+)"'


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if m := re.search(r'<iframe[^>]*src="(?P<https>https?://)?(?P<www>www\.)?youtube\.com(?P<embed>/embed/)(?P<ID>[\w-]+)"', s):
       return f"https://youtu.be/{m.group("ID")}"
    return None


if __name__ == "__main__":
    main()
