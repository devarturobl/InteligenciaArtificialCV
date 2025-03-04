import cv2

# Cargar el clasificador Haar Cascade para detección de cuerpo completo
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Iniciar la captura de video (puede ser una cámara web o un archivo de video)
cap = cv2.VideoCapture(0)  # 0 para la cámara web

while True:
    # Leer el fotograma de la cámara
    ret, frame = cap.read()
    
    if not ret:
        print("No se pudo capturar el video.")
        break

    # Convertir el fotograma a escala de grises para mejorar la detección
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ajustar los parámetros de detectMultiScale
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar un recuadro alrededor de los cuerpos detectados
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Recuadro rojo

    # Mostrar el fotograma con los recuadros
    cv2.imshow('Detección de Cuerpo Completo', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas abiertas
cap.release()
cv2.destroyAllWindows()
