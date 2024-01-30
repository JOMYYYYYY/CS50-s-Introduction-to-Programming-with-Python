import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >2 :
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            count_lines = 0
            filename = sys.argv[1]
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        count_lines = count_lines + 1
            print(count_lines)
        except FileNotFoundError:
            sys.exit("File does not exist")