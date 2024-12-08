import cv2

cap = cv2.VideoCapture("D:/ia/OpenCV/videos/runners.mp4")
if not cap.isOpened():
    print("Erro: Não foi possível abrir o vídeo.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
