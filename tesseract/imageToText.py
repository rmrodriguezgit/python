import pytesseract as tess
from PIL import Image



tess.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'


img = Image.open('prueba.png')
text = tess.image_to_string(img)

print(text)
