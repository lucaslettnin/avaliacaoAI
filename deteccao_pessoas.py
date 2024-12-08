import cv2
import numpy as np

contador_pessoas = 0

def detec_blobs(frame):
    global contador_pessoas
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contador_pessoas = len(contours)
    for contour in contours:
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)
    return frame

def contagem_pessoas(video):
    global contador_pessoas
    cap = cv2.VideoCapture(video)

    if not cap.isOpened():
        print("Erro: Não foi possível abrir o vídeo.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o quadro ou vídeo terminou.")
            break

        frame = detec_blobs(frame)
        cv2.putText(frame, "Pessoas: {}".format(contador_pessoas), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow('Contagem de Pessoas', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

contagem_pessoas("D:/ia/OpenCV/videos/runners.mp4")

