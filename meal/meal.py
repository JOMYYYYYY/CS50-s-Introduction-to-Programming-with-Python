def main():
    m=input("What time is it?")
    times=convert(m)
    if 7<=times<=8:
        print("breakfast time")
    elif 12<=times<=13:
        print("lunch time")
    elif 18<=times<=19:
        print("dinner time")


def convert(time):
    a,b=time.split(":")
    a=float(a)
    b=float(b)
    c=a+b/60
    return c

if __name__ == "__main__":
    main()