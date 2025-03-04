import cv2
import mediapipe as mp

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir la imagen a RGB (MediaPipe trabaja con RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Procesar la imagen con MediaPipe Hands
    results = hands.process(rgb_frame)
    
    # Dibujar los resultados en la imagen original
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Mostrar la imagen
    cv2.imshow('Hand Detector', frame)
    
    # Salir con la tecla 'q'pip 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
