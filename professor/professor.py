import random


def main():
    r_times = 0
    my_level = get_level()
    for i in range(10):
        e_times = 0
        x = generate_integer(my_level)
        y = generate_integer(my_level)
        z = x + y
        print(str(x) + " + " + str(y) + " = ")
        while True:
            my_answer = input()
            if my_answer.isnumeric():
                if int(my_answer) == z:
                    r_times = r_times + 1
                    break
                else:
                    print("EEE")
                    e_times = e_times + 1
                    if e_times == 3:
                        print(str(x) + " + " + str(y) + " = " + str(z))
                        break
                    pass
    print(r_times)

def get_level():
    while True:
        try:
            level = input("Level: ")
            if level in ["1", "2", "3"]:
                level = int(level)
                break
        except ValueError:
            pass
    return level



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else: # level is 3
        return random.randint(100, 999)


if __name__ == "__main__":
    main()

    # check50 cs50/problems/2022/python/professor