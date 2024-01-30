import sys
import csv

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
else:
    try:
        students = []
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                full_name = row["name"].strip('"')
                # print(full_name)
                last_name, first_name = full_name.split(", ")
                house = row["house"]
                student = {"first_name": first_name, "last_name": last_name, "house": house}
                students.append(student)
        with open(sys.argv[2], "w") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=["first_name", "last_name", "house"])
            writer.writerow({"first_name": "first", "last_name": "last", "house": "house"})
            for student in students:
                writer.writerow(student)
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
