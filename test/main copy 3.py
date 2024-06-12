import cv2
import deepsparse
from deepsparse import Engine
import numpy as np

# Путь к ONNX-файлу предварительно обученной модели YOLOv8
MODEL_PATH = "path/to/yolov8/onnx/model"

# Загрузка модели с помощью DeepSparse Engine
engine = Engine(MODEL_PATH)

def preprocess(frame):
    """
    Препроцессинг кадра для подачи в модель.
    Следует выполнить масштабирование и нормализацию согласно требованиям модели.
    """
    resized_frame = cv2.resize(frame, (640, 640))  # Пример изменения размера
    img = resized_frame.astype("float32")
    img = img.transpose(2, 0, 1)  # Меняем порядок каналов
    img = np.expand_dims(img, 0)  # Добавляем батч размерность
    return img

def draw_predictions(frame, detections):
    """
    Отображение результатов детекции на кадре.
    """
    for detection in detections[0]:  # Предполагается, что detections - это список батчей
        x1, y1, x2, y2, conf, cls = detection[:6]
        if cls == 0:  # Предполагаем, что класс 0 соответствует человеку
            start_point = (int(x1), int(y1))
            end_point = (int(x2), int(y2))
            color = (255, 0, 0)
            thickness = 2
            cv2.rectangle(frame, start_point, end_point, color, thickness)

    cv2.imshow("Frame", frame)

# Инициализация захвата видео
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = preprocess(frame)
    predictions = engine.run(processed_frame)
    draw_predictions(frame, predictions)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Выход по нажатию клавиши 'q'
        break

cap.release()
cv2.destroyAllWindows()
