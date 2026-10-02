import cv2

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)                          # efecto espejo (más natural)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # blanco y negro
   # cv2.circle(frame, (320, 240), 50, (0, 255, 0), 3)   # dibuja un círculo verde

    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

