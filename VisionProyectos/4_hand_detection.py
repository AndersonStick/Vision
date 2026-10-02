import cv2
import numpy as np
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.5)

PUNTAS = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)                 # efecto espejo
    alto, ancho, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # MediaPipe usa RGB
    resultado = hands.process(rgb)

    if resultado.multi_hand_landmarks:
        for mano in resultado.multi_hand_landmarks:
            puntos = []
            for i in PUNTAS:
                lm = mano.landmark[i]
                x, y = int(lm.x * ancho), int(lm.y * alto)   # a píxeles
                puntos.append((x, y))
                cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

            # unir los puntos en una figura cerrada
            cv2.polylines(frame, [np.array(puntos)], True, (255, 0, 255), 2)

    cv2.imshow("Manos", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()