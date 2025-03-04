#Agenda del día Viernes 31 de enero
# 1 Crear una aplicacion que permita cargar dos imagenes
# 2 Convertir una escala de grises
# 3 Redimensionar las imagenes
# 4 Dibujar Sobre Ventana

import cv2 as cv
import numpy as np

#obtener una imagen de archivo
img_personas = cv.imread('personas.jpg', 1)
img_negros = cv.imread('negros.jpg', 1)

#mostrar una imagen
cv.imshow("Personas",img_personas)
cv.imshow("Negros",img_negros)

#Convertir imagenes a escala de gris
cg_imgpersonas = cv.cvtColor(img_personas, cv.COLOR_BGR2GRAY)
cg_imgnegros = cv.cvtColor(img_negros, cv.COLOR_BGR2GRAY)

#mostrar una imagen Nota Los nombre de las ventanas deben ser diferentes
cv.imshow("Personas1",cg_imgpersonas)
cv.imshow("Negros1",cg_imgnegros)

#Redimencionar las imagenes
rpersonas = cv.resize(cg_imgpersonas, (300,300))
rnegros = cv.resize(cg_imgnegros, (200,300))
cv.imshow("Personas2",rpersonas)
cv.imshow("Negros2",rnegros)

#Comentar si queremos ver las imagenes anteriores
#cv.destroyAllWindows()

#Crear una imagen en negro
imagen_negra = np.zeros((500, 500, 3), dtype="uint8")

#Dibujar una linea recta
cv.line(imagen_negra, (50, 250), (450, 250), (0, 255, 0), 3)
cv.line(imagen_negra, (250, 50), (250, 450), (0, 255, 0), 3)

# Dibujar un rectángulo
cv.rectangle(imagen_negra, (50, 50), (450, 450), (255, 0, 0), 3)

# Dibujar un círculo con parametro 1 es sin relleno con parametro 0 con relleno
cv.circle(imagen_negra, (250, 250), 200, (0, 0, 255), 1)

#Detectar los bordes de una imagen
bordes = cv.Canny(rpersonas, 300, 300)  # Límite inferior y superior
cv.imshow("Detección de Bordes", bordes)

cv.imshow("Ventana Negra", imagen_negra)
#Pausa
cv.waitKey(0)

#Cerrar la carga de memoria
cv.destroyAllWindows()