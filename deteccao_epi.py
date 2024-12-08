import cv2
import numpy as np

def detect_epi(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 70, 50])
    upper_red = np.array([10, 255, 255])
    lower_green = np.array([40, 70, 50])
    upper_green = np.array([70, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.bitwise_or(mask_red, mask_green)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)

def main():
    image_path = 'path/to/your/image.jpg'
    image = cv2.imread(image_path)
    if image is None:
        print("Erro: Não foi possível carregar a imagem.")
        return

    epi_count = detect_epi(image)
    print('Quantidade de EPIs detectados: ', epi_count)

if __name__ == '__main__':
    main()
