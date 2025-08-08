from PIL import Image
import pytesseract
import pathlib
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
translator = Translator()

text = ""
ans = input("Do you want the photos to be translated into Persian?(y/n): ")

if pathlib.Path("per_pics").exists():
    for path in pathlib.Path("per_pics").iterdir():
        if path.is_file():
            img = path
            text += pytesseract.image_to_string(Image.open(img), lang="fas")
            text += 50 * "_"
else:
    print("Folder 'per_pics' not found.")

if pathlib.Path("eng_pics").exists():
    for path in pathlib.Path("eng_pics").iterdir():
        if path.is_file():
            img = path
            eng = pytesseract.image_to_string(Image.open(img), lang="eng")
            if "y" in ans.lower():
                text += translator.translate(eng, src="en", dest="fa").text
            else:
                text += eng
            text += 50 * "_"
else:
    print("Folder 'eng_pics' not found.")

with open("text.txt", "w", encoding="utf8") as f:
    f.write(text)

print("✅ Text extraction completed. File saved as text.txt")

# 