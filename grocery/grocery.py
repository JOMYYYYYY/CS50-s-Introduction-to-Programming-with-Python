original_dict = {}
count = 0
flag = True
while flag:
    try:
        key = input().strip()
    except EOFError:
        flag = False
    else:
        key = key.lower().capitalize()
        if key in original_dict: # check whether key has already existed
            original_dict[key] += 1
            count = original_dict[key]
        else:
            original_dict.update({key:1})
        # original_dict.update({key: count})
        # add a key ; the count shows that how many times key has been input
sorted_dict = sorted(original_dict.keys())
for i in sorted_dict:
    print(str(original_dict[i])+" "+f"{i.upper()}")