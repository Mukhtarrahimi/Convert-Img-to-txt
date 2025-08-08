from PIL import Image
import pytesseract
import pathlib
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
translator = Translator()

text = ""
ans = input("Do you want the photos to be translated into Persian?(y/n): ")

for path in pathlib.Path("per_pics").iterdir():
    if path.is_file():
        img = path
        text += pytesseract.image_to_string(Image.open(img), lang="fas")
        text += 50 * "_"
