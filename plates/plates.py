import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length_of_s = len(s)
    if length_of_s < 2 or length_of_s > 6:
        return False

    s_list = list(s)
    letter1 = s_list[0].isalpha()
    letter2 = s_list[1].isalpha()
    if not (letter2 and letter1):
        return False

    for i in s_list:
        if i == " " or i in string.punctuation:
            return False

    if s[-1].isnumeric():
        num = []
        while s[-1].isnumeric():
            num.append(s[-1])
            s = s[:-1]
        for i in s:
            if i.isdigit():
                return False
        if int(num[-1]) == 0:
            return False
    else:
        for i in s:
            if i.isdigit():
                return False

    return True


main()
