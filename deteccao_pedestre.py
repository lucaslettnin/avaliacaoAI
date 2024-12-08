import cv2

pedestrian_detector = cv2.HOGDescriptor()
pedestrian_detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture("D:/ia/OpenCV/videos/runners.mp4")
if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o quadro2.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bbox, _ = pedestrian_detector.detectMultiScale(gray, winStride=(4, 4), padding=(8, 8), scale=1.05)

    for i in range(len(bbox)):
        cv2.rectangle(frame, (bbox[i][0], bbox[i][1]), (bbox[i][0] + bbox[i][2], bbox[i][1] + bbox[i][3]), (0, 255, 0), 2)

    cv2.imshow('Pedestrian Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
