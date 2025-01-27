#Libreria de opencv
import cv2 as cv;

#Libreria para cargar imagenes
myImage = cv.imread('cocacola.png', 1)
#Cambiar tamaño de la imagen
myImage = cv.resize(myImage, (200, 200))

#Libreria para mostrar imagenes
cv.imshow('CocaCola Imagen Original', myImage)

#Convertir la imagen a RGB
myImage_RGB = cv.cvtColor(myImage, cv.COLOR_BGR2RGB)
myImage_RGB = cv.resize(myImage_RGB, (200, 200))
#Mostrar la imagen RGB
cv.imshow('CocaCola Imagen RGB', myImage_RGB)

#convertir imagen a escala de grises
myImage_GRAY = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)
myImage_GRAY = cv.resize(myImage_GRAY, (200, 200))
#MOSTRAR IMAGEN GRAY
cv.imshow('CocaCola Imagen GRAY', myImage_GRAY)

#Convertir imagen en HSV
myImage_HSV = cv.cvtColor(myImage, cv.COLOR_BGR2HSV)
myImage_HSV
cv.imshow('CocaCola Imagen HSV', myImage_HSV)

#Pausar una pantalla
cv.waitKey(0)
#Terminar la ejecucin de mi programa
cv.destroyAllWindows()
