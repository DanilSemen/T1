import cv2
import time
from deepsparse import DeepSparse
from yolov8 import YOLOv8

# Инициализация модели YOLOv8 для обнаружения объектов класса "person"
yolo = YOLOv8(weights='yolov8.weights', config='yolov8.cfg', classes=['person'])

# Инициализация DeepSparse для ускорения обработки
deepsparse = DeepSparse()

# Открытие веб-камеры
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Не удалось прочитать видеопоток")
        break

    # Предобработка кадра
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обнаружение объектов с помощью YOLOv8
    start_time = time.time()
    detections = yolo.detect(processed_frame)
    print(f"Время обнаружения объектов: {time.time() - start_time} сек")

    # Ускорение обработки с помощью DeepSparse
    start_time = time.time()
    processed_frame_fast = deepsparse.process(frame)
    print(f"Время ускоренной обработки: {time.time() - start_time} сек")

    # Отображение результатов
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Processed Frame', processed_frame_fast)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
