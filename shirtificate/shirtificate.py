from fpdf import FPDF
from PIL import Image

name = input("Name: ")
pdf = FPDF(orientation="Portrait", format="A4")
pdf.add_page()
pdf.set_font("Arial", size=35)

# Get the width of the text
text_width1 = pdf.get_string_width("CS50 Shirtificate")

# Calculate the x-coordinate to center the text
x1 = (pdf.w - text_width1) / 2
pdf.text(x1, 40, "CS50 Shirtificate")
pdf.image("shirtificate.png", x=6, y=65, w=200, h=200)

# Set the color of the text to white
pdf.set_text_color(255, 255, 255)


text_on_shirt = name + " took CS50"
# Add the text in the middle of the image
pdf.set_xy(6, 65)
text_width2 = pdf.get_string_width(text_on_shirt)
x2 = (pdf.w - text_width2)/2
pdf.text(x2, 130, text_on_shirt)

pdf.output("shirtificate.pdf")