
import onnxruntime as ort
import cv2
import numpy as np

# Загрузка модели ONNX
session = ort.InferenceSession("yolov8n.onnx")

# Функция для выполнения инференса
def detect_objects(frame):
    input_blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(640, 640), swapRB=True, crop=False)
    input_blob = np.expand_dims(input_blob, axis=0)

    # Выполнение инференса
    outputs = session.run(None, {session.get_inputs()[0].name: input_blob})
    return outputs

# Открытие видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Выполнение инференса
    detections = detect_objects(frame)

    # Обработка результатов детекции
    for detection in detections[0]:
        confidence = detection[4]
        if confidence > 0.5:
            box = detection[:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
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