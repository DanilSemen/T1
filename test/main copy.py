import tensorflow as tf
import cv2
import numpy as np

# Убедитесь, что TensorFlow использует GPU
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
    print("GPU is available and will be used for inference")

# Загрузка модели YOLOv8
model = tf.saved_model.load('/yolov8n.pt')

# Функция для выполнения инференса
def detect_objects(frame):
    input_tensor = tf.convert_to_tensor(frame)
    input_tensor = input_tensor[tf.newaxis, ...]

    detections = model(input_tensor)

    return detections

# Открытие видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Выполнение инференса
    detections = detect_objects(frame)

    # Обработка результатов детекции
    for detection in detections:
        confidence = detection['confidence']
        if confidence > 0.5:
            box = detection['box']
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            label = f"{confidence * 100:.2f}%"
            cv2.putText(frame, label, (startX, startY - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Отображение результата
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()