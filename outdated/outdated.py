def check_valid1(str):  # check whether input in valid MM/DD/YYYY format
    # if len(str) != 10:
    #     print("len")
    #     return False
    if not "/" in str:
        # print("do not have /")
        return False
    else:
        part = str.split("/")
        if not part[0].isdigit():
            # print("digit")
            return False
        if not part[1].isdigit():
            return False
        if not part[2].isdigit():
            return False
        else:
            part[0], part[1], part[2] = int(part[0]), int(part[1]), int(part[2])
            if (part[0] in range(1, 12)) and (part[1] in range(1, 31)) and (part[2] in range(1000, 9999)):
                # print(part)
                return True
            else:
                # print(part[0])
                return False


def get_1(str):
    m_str, d_str, y_str = str.split("/")
    return y_str, m_str, d_str


def check_valid2(str):  # check whether input in valid <September 8, 1636> format
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    month_dict = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    part = str.split()
    if len(part) == 3 and part[0] in month_list and part[1].endswith(",") and part[1].replace(",", "").isdigit() and \
            part[2].isdigit() and int(part[1][:-1]) in range(1, 31):
        return True
    else:
        return False


def get_2(str):
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    month_dict = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    part = str.split()
    return part[2], month_dict[part[0]], part[1].replace(",", "")


def main():
    while True:
        date_string = input("Date: ").strip().lower().title()
        # first: check whether the input is in the valid format;

        # second: use two method to convert each valid input into YYYY-MM-DD format. then break.
        if check_valid1(date_string):  # convert MM/DD/YYYY format
            y_str, m_str, d_str = get_1(date_string)
            # print(y_str + "-" + f"{int(m_str):02}" + "-" + f"{int(d_str):02}")
            break
        if check_valid2(date_string):  # convert <September 8, 1636> format
            y_str, m_str, d_str = get_2(date_string)
            # print(y_str + "-" + f"{int(m_str):02}" + "-" + f"{int(d_str):02}")
            break
        # third: print the YYYY-MM-DD format string
    print(y_str + "-" + f"{int(m_str):02}" + "-" + f"{int(d_str):02}")
main()
