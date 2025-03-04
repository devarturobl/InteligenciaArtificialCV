import cv2 as cv
import numpy as np

#1 Decalar una variable = webcam
camara = cv.VideoCapture(1)

#Crear un ciclo while para mantener la captura de la camara
while True:
    ret, frame = camara.read()

    if not ret:
        print("La esta inactiva")
        break

    #Mostrar en una ventana los frame capturados
    cv.imshow('WebCam Live', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#Nota despues de ocupar la camara hay que vaciar el buffer
camara.release()
cv.destroyAllWindows()
