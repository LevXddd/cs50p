import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # it must start with decimal
    if m := re.search(r"^(?P<h1>[\d]{1,2})(?P<m1>:[\d]{2})? (?P<p1>AM|PM) to (?P<h2>[\d]{1,2})(?P<m2>:[\d]{2})? (?P<p2>AM|PM)$", s, re.IGNORECASE):
        start = to_24(m.group("h1"), m.group("m1"), m.group("p1"))
        end   = to_24(m.group("h2"), m.group("m2"), m.group("p2"))
    else:
        raise ValueError

    return f"{start} to {end}"


def to_24(hours, minutes, period):
    if minutes is None:
        minutes = ":00"
    hours = int(hours)
    num = int(minutes[1:])      # strip the colon → "00" → 0
    if not (1 <= hours <= 12):
        raise ValueError
    if not (0 <= num <= 59):
        raise ValueError
    if period == "PM" and hours != 12:
        hours = hours + 12
        time = f"{hours:02d}{minutes}"
        return time
    elif period == "PM" and hours == 12:
        return f"{12}{minutes}"
    elif period == "AM" and hours != 12:
        return f"{hours:02d}{minutes}"
    elif period == "AM" and hours == 12:
        return f"00{minutes}"



if __name__ == "__main__":
    main()
