from PIL import Image
from pytesseract import pytesseract
import re
import csv

pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('credit_card.png')
txt = pytesseract.image_to_string(img, lang = 'eng')

txt = re.findall(r'[0-9]{4} [0-9]{4} [0-9]{4}',txt)
for str in txt:
    txt=str

with open('credit_card.csv',mode='r') as file:

    csvfile=csv.reader(file)

    for lines in csvfile:
        if txt in lines:
            print("Not fake")
            break
    else:
        print("fake")
        


