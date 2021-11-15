try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyautogui as pg
from time import sleep as s

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

s(3)

pg.screenshot("Python/HumanBenchmark/Typing/Text.png", region=(459,383, 1000,220))

text = pytesseract.image_to_string(Image.open('Python/HumanBenchmark/Typing/Text.png'))

print(text)

pg.write(text)