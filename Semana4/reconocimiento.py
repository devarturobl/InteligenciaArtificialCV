import cv2
import pytesseract


image = cv2.imread('descarga.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

text = pytesseract.image_to_string(image,lang='spa')
print('Texto: ',text)
      
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()



