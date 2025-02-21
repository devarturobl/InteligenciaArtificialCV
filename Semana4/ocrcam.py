import cv2 as cv
import pytesseract as pt
import numpy as np

cam = cv.VideoCapture(0)
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

while True:
    ret, frame = cam.read()

    gris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    text = pt.image_to_string(gris,lang='spa')
    print('Texto: ',text)

    if not ret:
        print("La esta inactiva")
        break

    cv.imshow('WebCam Live', frame)


    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()  