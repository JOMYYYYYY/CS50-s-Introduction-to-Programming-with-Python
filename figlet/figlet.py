import sys
import pyfiglet
import random

figlet_object = pyfiglet.Figlet()  # creat a Figlet Objet
font_list = figlet_object.getFonts()  # gather all of the fonts in a list
if len(sys.argv) == 3:
    if ((sys.argv[1] == "-f") or (sys.argv[1] == "--font")) and sys.argv[2] in font_list:
        original_text = input("input text= ").strip()
        font_style = sys.argv[2]
        figlet_object.setFont(font=font_style)
        art_text = figlet_object.renderText(original_text)
        print(art_text)
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    font_style = random.choice(font_list)  # randomly get a font from the list
    figlet_object.setFont(font=font_style)  # set the font to the fig object
    original_text = input("input text= ").strip()
    art_text = figlet_object.renderText(original_text)
    print(art_text)
else:
    sys.exit("Invalid usage")

