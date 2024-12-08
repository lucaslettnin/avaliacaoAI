import cv2
import numpy as np
import tensorflow as tf
import json

def main():
    model = tf.keras.models.load_model('path/to/handpose/model')

    with open('path/to/handpose/params.json') as f:
        params = json.load(f)

    cap = cv2.VideoCapture("D:/ia/OpenCV/videos/runners.mp4")
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a câmera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o quadro4.")
            break

        resized_frame = cv2.resize(frame, (256, 256))
        resized_frame = np.expand_dims(resized_frame, axis=0)
        prediction = model.predict(resized_frame)

        cv2.imshow('Reconhecimento de Libras', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
