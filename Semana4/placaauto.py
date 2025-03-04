import cv2 as cv
import pytesseract as ocr
import numpy as np
import re

placa = []

image = cv.imread('auto.jpg')
img2 = cv.imread('auto.jpg')
cv.imshow('Imagen normal', image)
#cambiar el color a gris
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Imagen en gris', gray)
#aplicar filtro de distorsion
gray = cv.blur(gray, (3,3))
cv.imshow('Imagen con filtro blur', gray)
#aplicar controno
canny = cv.Canny(gray, 150, 200)
cv.imshow('Imagen con filtro canny', canny)
#Aplicar relieve
canny = cv.dilate(canny, None, iterations=1)
cv.imshow('Imagen con filtro dilate', canny)

#importamos la ruta de libreria
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Encontrar los contornos
cnts, _ = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image,cnts,-1,(0,255,0),2)
cv.imshow('Imagen con contornos', image)    

for c in cnts:
  area = cv.contourArea(c)
  x,y,w,h = cv.boundingRect(c)
  epsilon = 0.09*cv.arcLength(c,True)
  approx = cv.approxPolyDP(c,epsilon,True)
  
  if len(approx)==4 and area>9000:
    print('area=',area)
    #cv2.drawContours(image,[approx],0,(0,255,0),3)
    aspect_ratio = float(w)/h
    if aspect_ratio>2.4:
      placa = gray[y:y+h,x:x+w]
      text = ocr.image_to_string(placa, config='--psm 11')
      
      # Limpiar el texto detectado
      text = re.sub(r'[^a-zA-Z0-9]', '', text)  # Eliminar caracteres no alfanuméricos
      print('PLACA: ', text)

      #cv.imshow('PLACA',placa)
      #cv.moveWindow('PLACA',780,10)
      cv.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),3)
      cv.putText(img2, text, (x-20, y-10), 1, 2.2, (0,255,0), 3)

    cv.imshow('Resultado', img2)
#cv.moveWindow('Resultado',45,10)
cv.waitKey(0)