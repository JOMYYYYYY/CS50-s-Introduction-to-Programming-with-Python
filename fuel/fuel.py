flag = True
while flag:
    text = input("prompt")
    if not any(c == "/" for c in text):
        pass
    else:
        parts = text.split("/")
        a = parts[0]
        b = parts[1]
        try:
            a = int(a)
            b = int(b)
            c = float(a / b)
            if a > b:
                pass
            else:
                if c <= 0.01:
                    print("E")
                elif c >= 0.99:
                    print("F")
                else:
                    c = int(round(c, 2)*100)
                    print(f"{c}%")
                break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


