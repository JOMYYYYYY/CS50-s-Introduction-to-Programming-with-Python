"""
total = 50
a = int(input("Insert Coin: "))
if a!=25 and a!=10 and a!=5:
    print("Amount Due: 50")
while (a == 25 or a == 10 or a == 5) and (total >= 0):
    if total == 0:
        print("Change Owed: 0")
        break
    elif total > 0:
        total = total - a
        print("Amount Due: " + str(total))
        a = int(input())
        total = total - a
"""

total = 50
a = int(input("Insert Coin: "))
count = a
if a != 25 and a != 10 and a != 5:
    print("Amount Due: 50")
while (a == 25 or a == 10 or a == 5) and (count <= 50):
    if count == 50:
        print("Change Owed: 0")
        break
    elif total > 0:
        print("Amount Due: " + str(total - count))
    a = int(input("Insert Coin: "))
    count += a
if count > 50:
    print("Change Owed: " + str(count-total))
