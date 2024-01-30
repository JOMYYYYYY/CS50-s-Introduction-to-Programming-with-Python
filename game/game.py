
import random
while True:
    n = input("level: ")
    if n.isnumeric():
        n = int(n)
        if n > 0:
            random_n = random.randint(1, n)
            break
        else:
            pass
    else:
        pass

while True:
    guess_value = input("Guess: ")
    if guess_value.isnumeric():
        guess_value = int(guess_value)
        if guess_value > 0:
            if guess_value < random_n:
                print("Too small!")
                pass
            elif guess_value > random_n:
                print("Too large!")
                if guess_value > n:
                    print("Looks like you’re guessing outside the range you specified.")
                pass
            else:
                print("Just right!")
                break
        else:
            pass
    else:
        pass

