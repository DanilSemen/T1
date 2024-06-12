import os
import psutil
from motor.motor3 import *
from motor.control import *
from motor.control import stop_x, stop_y, move_x, move_y
from datetime import datetime
from vision.state import state
from collections import deque
import numpy as np

# Задаем аффинитет (привязку) процесса к одному ядру
pid = os.getpid()
p = psutil.Process(pid)
p.cpu_affinity([0,1,2,3,4,5,6,7])  # номер ядра, которое мы хотим использовать

import cv2
from ultralytics import YOLO
import threading
import torch

model = YOLO('yolov8n.onnx') 
# model = YOLO('yolov8n.rknn') 
# model = YOLO('yolov81.pt') 

# Открываем веб-камеру
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
if not cap.isOpened():
    print("Не удалось открыть веб-камеру")
    exit()

# # Устанавливаем стойболее низкое разрешение для ускорения обработки
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame = None
running = True
results = None
res =[]

# Создание очереди для отслеживания объектов
object_tracker = deque(maxlen=10)

def capture_and_display(cpu_cores):
    os.sched_setaffinity(0, cpu_cores)
    print(f"capture_and_display: Привязка к ядрам {cpu_cores}")
    global frame, running
    while running:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Рисуем красную точку в центре кадра
        frame = draw_center_dot(frame)        

        if results is not None:
            # frame_with_boxes = draw_boxes(frame.copy(), results)
            frame_with_boxes = draw_boxes_and_center(frame.copy(), results)
            cv2.imshow('Webcam', frame_with_boxes)
        else:
            cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False
            break

def draw_boxes_and_center(frame, results):
    person_detected = False  # Флаг для обнаружения человека
    # Проходим по результатам и рисуем рамки вокруг объектов
    for result in results[0].boxes:
        if int(result.cls) == 0 and result.conf >= 0.5:  # Класс 0 соответствует человеку
            x1, y1, x2, y2 = map(int, result.xyxy[0])
            # # Рисуем прямоугольник вокруг объекта
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # # Подписываем объект
            cv2.putText(frame, 'Person', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Определение центра координат объекта
            centerX, centerY = (x1 + x2) // 2, (y1 + y2) // 2

            # Рисуем красную точку в центре объекта
            cv2.circle(frame, (centerX, centerY), 5, (0, 0, 255), -1)

            # # Рисуем квадрат вокруг центра обнаруженного объекта
            square_dim = int(min(x2 - x1, y2 - y1) * 0.1)
            cv2.rectangle(frame, (centerX - square_dim, centerY - square_dim), (centerX + square_dim, centerY + square_dim), (255, 0, 0), 2)

            person_detected = True  # Человек обнаружен
            current_time = datetime.now()
            # print(current_time.strftime("%Y-%m-%d %H:%M:%S.%f"))
            # print("ВНИМАНИЕ ЧЕЛОВЕК")
    if not person_detected:  # Если человек не обнаружен
        stop_x()  # Остановить двигатели
        stop_y()  # Остановить двигатели

    return frame

def draw_center_dot(frame):
    """
    Рисует красную точку в центре кадра.
    :param frame: текущий кадр видео
    :return: кадр с нарисованной точкой
    """
    height, width = frame.shape[:2]  # Получаем размеры кадра
    center_coordinates = (width // 2, height // 2)  # Вычисляем центр кадра

    # Рисуем красную точку в центре кадра
    # (0, 0, 255) означает красный цвет в формате BGR, 5 это размер точки
    cv2.circle(frame, center_coordinates, 5, (0, 0, 255), -1)

    return frame


# def process_frame(cpu_cores):
#     os.sched_setaffinity(0, cpu_cores)
#     global frame, running, results
        
#     while running:
#         if frame is not None:
#             results = model(frame)
#             height, width = frame.shape[:2]
#             center_x, center_y = width // 2, height // 2
            
#             for result in results[0].boxes:
#                 if int(result.cls) == 0:  # Предполагаем, что класс 0 соответствует интересующему нас объекту
#                     x1, y1, x2, y2 = map(int, result.xyxy[0])
#                     obj_center_x, obj_center_y = (x1 + x2) // 2, (y1 + y2) // 2
#                     state.update(frame, running, results, center_x, center_y, obj_center_x, obj_center_y, x1, y1, x2, y2)
#                     # move_x(state.center_x, state.center_y, state.obj_center_x, state.obj_center_y, state.x1, state.y1, state.x2, state.y2)
#                     # move_y(state.center_x, state.center_y, state.obj_center_x, state.obj_center_y, state.x1, state.y1, state.x2, state.y2)
                    
#     return state.center_x, state.center_y, state.obj_center_x, state.obj_center_y, state.x1, state.y1, state.x2, state.y2
                    
                 
# Указываем ядра процессора для каждой функции
# process_cpu_cores = {1,2,3,4,5,6,7}   # Ядра для захвата кадров и отображения окна
# capture_cpu_cores = {0} # Ядро для обработки YOLOv8



# # Указываем ядра процессора для каждой функции
process_cpu_cores = {0}  # Ядра для захвата кадров и отображения окна
capture_cpu_cores = {1,2,3,4,5,6,7}  # Ядро для обработки YOLOv8


