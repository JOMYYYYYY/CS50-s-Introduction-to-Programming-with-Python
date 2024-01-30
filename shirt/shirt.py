import sys
import os
from PIL import Image

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments ")
    else:
        sys.exit("Too many command-line arguments")
else:
    file_name_1 = sys.argv[1]
    file_name_2 = sys.argv[2]

    base_name_1, extention_1 = os.path.splitext(file_name_1)
    base_name_2, extention_2 = os.path.splitext(file_name_2)
    extention_1 = extention_1.lower()
    extention_2 = extention_2.lower()
    if not ((extention_1 == ".jpg" or extention_1 == "jpeg" or extention_1 == ".png") and (
            extention_2 == ".jpg" or extention_2 == "jpeg" or extention_2 == ".png")):
        sys.exit("Invalid output")
    elif extention_1 != extention_2:
        sys.exit("Input and output have different extensions")
    else:
        try:
            original_body_pic_object = Image.open(file_name_1)
            shirt = Image.open("shirt.png")

            size_of_body_pic = original_body_pic_object.size
            size_of_shirt_pic = shirt.size
            print(size_of_body_pic)
            print(size_of_shirt_pic)

            original_body_pic_object = original_body_pic_object.resize((600, 800))
            original_body_pic_object.paste(shirt, (0, 100), shirt)
            new_image_object = original_body_pic_object
            new_image_object = new_image_object.crop((0, 100, 600, 700))
            new_image_object.save(file_name_2)


        except FileNotFoundError:
            sys.exit("Input does not exist")
