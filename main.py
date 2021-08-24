import cv2
import PIL
from PIL import Image
import pafy
import pytesseract
import threading
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

count=0
def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text.strip()
url = "https://www.youtube.com/watch?v=OPasaabfxAo"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture()
capture.open(best.url)

success,image = capture.read()

while success:
    #cv2.imshow('frame', image)
    count+=100
    capture.set(1,count)
    if ocr_core(image):
        print(ocr_core(image))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    success,image = capture.read()

cv2.destroyAllWindows()
capture.release()
