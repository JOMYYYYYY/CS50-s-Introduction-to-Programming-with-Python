from datetime import date
import re
import sys
import inflect


def main():
    birth_date = input("Date of Birth: ")
    if check_input_validation(birth_date):
        # date.fromisoformat(birth_date) means that cast the str like "1909-08-89" into a date object
        birth_date = date.fromisoformat(birth_date)
        timedelta = date.today() - birth_date
        # timedelta = date(2000, 1, 1) - birth_date
        minutes = timedelta.days * 24 * 60
        p = inflect.engine()
        words = p.number_to_words(minutes).capitalize().replace(" and ", " ")
        # print(minutes)
        print(words + " minutes")
    else:
        sys.exit("Invalid date")


# a function to check if the input is valid or not
def check_input_validation(s):
    s = str(s).strip()
    if len(s) != 10:
        return False
    pattern = r"^([0-9]{4})-([0|1]{1}[0-9]{1})-([0-3]{1}[0-9]{1})"
    if match := re.match(pattern, s):
        if 0 <= int(match.group(1)) and 1 <= int(match.group(2)) <= 12 and 1 <= int(match.group(3)) <= 31:
            # print("Valid date of birth")
            return True
        else:
            return False
    else:
        return False


# a function to check if the year is leap year or not
# def is_leap_year(year):
#     year = int(year)
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False


# # a function to count how many leap years are there in the given list
# def count_leap_years(s):
#     count = 0
#     for i in s:
#         if is_leap_year(i):
#             count += 1
#     return count


if __name__ == "__main__":
    main()
