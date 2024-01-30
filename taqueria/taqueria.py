menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
count = 0
while True:
    try:
        items = input("prompt:")
        items = items.lower().title()
        for i in menu:
            if i == items:
                count += menu[i]
                print("Total: ${:.2f}".format(count))
        pass
    except EOFError:
        print("Total: ${:.2f}".format(count))
        break
    except KeyError:
        pass
