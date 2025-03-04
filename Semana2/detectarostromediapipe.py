import cv2
import mediapipe as mp

# Inicializar Face Mesh de MediaPipe
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Crear el objeto de detección de malla facial
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)  # 0 para cámara web

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el video.")
        break

    # Convertir a RGB (MediaPipe trabaja con imágenes en RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar la detección de la malla facial
    results = face_mesh.process(frame_rgb)

    # Si se detectan rostros, dibujar la malla sobre la cara
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                frame, 
                face_landmarks, 
                mp_face_mesh.FACEMESH_TESSELATION,  # Tipo de malla (conexiones entre puntos)
                mp_drawing_styles.get_default_face_mesh_tesselation_style(),  # Estilo de líneas
                mp_drawing_styles.get_default_face_mesh_landmarks_style()  # Estilo de puntos
            )

    # Mostrar la imagen con la malla facial
    cv2.imshow("Detector de Rostros con Malla (Face Mesh)", frame)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
