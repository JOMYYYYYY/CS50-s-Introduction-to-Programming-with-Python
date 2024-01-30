camel_case=input("camelCase:")
list = []
for i in camel_case:
    if i.isupper():
        list.append("_")
    list.append(i.lower())
sanke_case = "".join(list)
print(sanke_case)
