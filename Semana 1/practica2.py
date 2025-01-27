import cv2 as cv;
import numpy as np;

#Libreria para cargar imagenes
myImage = cv.imread('cuadritos.jpg', 1)

#Para este programa de decteción de color rojo
#cambiamos el formato de la imagen a hsv
myImage_HSV = cv.cvtColor(myImage, cv.COLOR_BGR2HSV)

#Definimos el rango de color rojo con np
lower_red1 = np.array([0, 150, 100])
upper_red1 = np.array([5, 255, 255])
lower_red2 = np.array([175, 150, 100])
upper_red2 = np.array([180, 255, 255])

#Creamos una mascara para el color rojo
mask1 = cv.inRange(myImage_HSV, lower_red1, upper_red1)
mask2 = cv.inRange(myImage_HSV, lower_red2, upper_red2)

#Unimos las dos mascaras esto es para la interface
mask = cv.add(mask1, mask2)

#Encontramos los contornos de la mascara
contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#dibujamos los contornos en la imagen original
for contour in contours:
    cv.drawContours(myImage, contour, -1, (255, 0, 0), 1)


#mostrar resultado
cv.imshow('CocaCola Imagen Original', myImage)
cv.imshow('Detector de Color Rojo', mask)

cv.waitKey(0)
cv.destroyAllWindows()
