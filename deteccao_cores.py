import cv2
import numpy as np

def capture_reference_image():
    cap = cv2.VideoCapture("D:/ia/OpenCV/videos/runners.mp4")
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a câmera.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o quadro.")
            break

        cv2.imshow('Reference Image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame

def perform_color_detection(frame, color, threshold):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color = np.array(color, dtype=np.uint8) - threshold
    upper_color = np.array(color, dtype=np.uint8) + threshold

    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    return res, mask

def init_color():
    print("Enter the color in (H, S, V) format: ")
    color = tuple(map(int, input().split()))
    print("Enter the threshold for color detection: ")
    threshold = int(input())
    return color, threshold

def main():
    color, threshold = init_color()
    ref_image = capture_reference_image()
    if ref_image is None:
        print("Erro ao capturar a imagem de referência.")
        return

    res, mask = perform_color_detection(ref_image, color, threshold)
    cv2.imshow('Result', res)
    cv2.imshow('Mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
