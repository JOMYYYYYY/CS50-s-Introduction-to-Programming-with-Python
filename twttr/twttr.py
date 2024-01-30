list_vowels = ["a","A","e","E","i","I","o","O","u","U"]
text = input("prompt:")
list_clean = []
for char in text:
    for i in list_vowels:
        if char == i:
            char = ""
    list_clean.append(char)
str1 = "".join(list_clean)
print(str1)