import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()

    # Convertir el frame a escala de grises (mejora la precisión de detección)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detectar rostros en el frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(faces)

    for (x, y, w, h) in faces:
        #cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Rectángulo verde
         # Centro del rostro
        center_x = x + w // 2
        center_y = y + h // 2

        # Definir el tamaño de las líneas de la cruz
        line_length = w-x

        # Dibujar las dos líneas que forman una cruz
        cv.line(frame, (center_x - line_length, center_y), (center_x + line_length, center_y), (0, 255, 0), 2)  # Línea horizontal
        cv.line(frame, (center_x, center_y - line_length), (center_x, center_y + line_length), (0, 255, 0), 2)  # Línea vertical


    #Mostar Video
    cv.imshow("Video Gris", frame)



    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
