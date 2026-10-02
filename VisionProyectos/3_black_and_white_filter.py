import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    b = frame[:, :, 0].astype(float)   # canal azul
    g = frame[:, :, 1].astype(float)   # canal verde
    r = frame[:, :, 2].astype(float)   # canal rojo

    gris = 0.299 * r + 0.587 * g + 0.0 * b
    gris = gris.astype(np.uint8)       # volver a números de 0 a 255

    cv2.imshow("Gris", gris)


   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

