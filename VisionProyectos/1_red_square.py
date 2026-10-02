import cv2

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    print(frame.shape)
    frame[0:100, 0:100] = (0, 0, 255)   # filas 0-100, columnas 0-100 → rojo

    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()