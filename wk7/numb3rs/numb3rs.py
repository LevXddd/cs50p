import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if m := re.search(r"^(?P<first>\d{1,3})\.(?P<second>\d{1,3})\.(?P<third>\d{1,3})\.(?P<fourth>\d{1,3})$", ip):
        if 0 <= int(m.group("first")) <= 255 and 0 <= int(m.group("second")) <= 255 and 0 <= int(m.group("third")) <= 255 and 0 <= int(m.group("fourth")) <= 255:
            if str(int(m.group("first"))) != m.group("first"):
                return False
            elif str(int(m.group("second"))) != m.group("second"):
                return False
            elif str(int(m.group("third"))) != m.group("third"):
                return False
            elif str(int(m.group("fourth"))) != m.group("fourth"):
                return False
            else:
                return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()


