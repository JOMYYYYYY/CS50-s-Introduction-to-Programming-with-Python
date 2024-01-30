import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            my_pizza = []

            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                for line in file:
                    pizza_type, small_pizza, large_pizza = line.strip().split(",")
                    pizzas = [pizza_type, small_pizza, large_pizza]
                    my_pizza.append(pizzas)
            print(tabulate(my_pizza, header, tablefmt="grid"))



    except FileNotFoundError:
        sys.exit("File does not exist")
