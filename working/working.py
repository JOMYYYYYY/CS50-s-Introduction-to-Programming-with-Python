import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)


def convert(s):
    # match format like "10 PM to 8 AM" or "9 AM to 5 PM"
    first_pattern = r"(1?[0-9]) (AM|PM) to (1?[0-9]) (AM|PM)"
    # match format like "9:00 AM to 5:00 PM" or "10:30 PM to 8:50 AM"
    second_pattern = r"(1?[0-9]):([0-5][0-9]) (AM|PM) to (1?[0-9]):([0-5][0-9]) (AM|PM)"
    if match_first_pattern := re.match(first_pattern, s):
        hour_first_pattern_1 = int(match_first_pattern.group(1))
        hour_first_pattern_2 = int(match_first_pattern.group(3))
        check_1 = match_first_pattern.group(2)
        check_2 = match_first_pattern.group(4)
        if hour_first_pattern_1 > 12 or hour_first_pattern_2 > 12:
            raise ValueError
        if hour_first_pattern_1 == 0 or hour_first_pattern_2 == 0:
            raise ValueError
        if hour_first_pattern_1 == 12:
            hour_first_pattern_1 = 0
        if hour_first_pattern_2 == 12:
            hour_first_pattern_2 = 0
        if check_1 == "PM":
            hour_first_pattern_1 += 12
        if check_2 == "PM":
            hour_first_pattern_2 += 12
        # convert to the format like "09:00 to 17:00"
        print_first_pattern = f"{hour_first_pattern_1:02}:00 to {hour_first_pattern_2:02}:00"
        return print_first_pattern
    elif match_second_pattern := re.match(second_pattern, s):
        hour_second_pattern_1 = int(match_second_pattern.group(1))
        minute_second_pattern_1 = int(match_second_pattern.group(2))
        hour_second_pattern_2 = int(match_second_pattern.group(4))
        minute_second_pattern_2 = int(match_second_pattern.group(5))
        check_1 = match_second_pattern.group(3)
        check_2 = match_second_pattern.group(6)
        if hour_second_pattern_1 == 12 and minute_second_pattern_1 != 0:
            raise ValueError
        if hour_second_pattern_2 == 12 and minute_second_pattern_2 != 0:
            raise ValueError
        if hour_second_pattern_1 == 0 and minute_second_pattern_1 == 0:
            raise ValueError
        if hour_second_pattern_2 == 0 and minute_second_pattern_2 == 0:
            raise ValueError
        if hour_second_pattern_1 == 12:
            hour_second_pattern_1 = 0
        if hour_second_pattern_2 == 12:
            hour_second_pattern_2 = 0
        if hour_second_pattern_1 > 12 or hour_second_pattern_2 > 12:
            raise ValueError
        if check_1 == "PM":
            hour_second_pattern_1 += 12
        if check_2 == "PM":
            hour_second_pattern_2 += 12
        # convert to the format like "09:00 to 17:00" or "22:30 to 08:50"
        print_second_pattern = f"{hour_second_pattern_1:02}:{minute_second_pattern_1:02} to {hour_second_pattern_2:02}:{minute_second_pattern_2:02}"
        return print_second_pattern
    else:
        raise ValueError


if __name__ == "__main__":
    main()
