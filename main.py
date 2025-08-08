from PIL import Image
import pytesseract
import pathlib
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
translator = Translator()

text = ""
ans = input("Do you want the photos to be translated into Persian?(y/n): ")
