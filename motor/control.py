
from vision.vision2 import *
# from vision.vision21 import *
from motor.motor3 import *
from motor.control import *
from vision.state import state
from time import sleep




# Допустим, у вас есть следующие функции для управления двигателями:
def move_up():
    # Код для активации двигателей для движения вверх
    print("Быстрое Движение вверх активировано")
    # motor2.step_motor(0, 100, 2000)
    motor2.stop()
    motor2.start_moving(direction=1)
def move_down():
    # Код для активации двигателей для движения вниз
    print("Быстрое Движение вниз активировано")
    # motor2.step_motor(1, 100, 2000)
    motor2.stop()
    motor2.start_moving(direction=0)

def move_left():
    # Код для активации двигателей для движения влево
    print("Быстрое  Движение влево активировано")
    # motor1.step_motor(1, 100, 2000)
    motor1.stop()
    motor1.start_moving(direction=1)


def move_right():
    # Код для активации двигателей для движения вправо
    print("Быстрое Движение вправо активировано")
    # motor1.step_motor(0, 100, 2000)
    motor1.stop()
    motor1.start_moving(direction=0)

def stop_x():    
    print("Двигатели остановлены")
    motor1.stop()
    

def stop_y():
    motor2.stop()
    print("Двигатели остановлены")


def move_up_low():
    # Код для активации двигателей для движения вверх
    print("Медленное Движение вверх активировано")
    # motor2.step_motor(0, 100, 2000)
    motor2.stop()
    motor2.start_moving_low(direction=1)
def move_down_low():
    # Код для активации двигателей для движения вниз
    print("Медленное  Движение вниз активировано")
    # motor2.step_motor(1, 100, 2000)
    motor2.stop()
    motor2.start_moving_low(direction=0)

def move_left_low():
    # Код для активации двигателей для движения влево
    print("Медленное Движение влево активировано")
    # motor1.step_motor(1, 100, 2000)
    motor1.stop()
    motor1.start_moving_low(direction=1)


def move_right_low():
    # Код для активации двигателей для движения вправо
    print("Медленное Движение вправо активировано")
    # motor1.step_motor(0, 100, 2000)
    motor1.stop()
    motor1.start_moving_low(direction=0)



# # функция запуска двигателя по горзонтали
# def move_x(center_x, center_y, obj_center_x, obj_center_y, x1, y1, x2, y2): 
#     # while True:

#         print("move_x")   
#         print("center_x", center_x, "center_y", center_y, "obj_center_x", obj_center_x, "obj_center_y", obj_center_y, "x1", x1, "y1", y1, "x2", x2, "y2", y2)
#         if center_x < x1:
#             move_right()
#         elif center_x > x1 and center_x < obj_center_x:
#             move_right_low()
#         if center_x > x2:
#             move_left()
#         elif center_x < x2 and center_x > obj_center_x:
#             move_left_low()
#         elif center_x == obj_center_x:
#             stop_x()
    
# # функция запуска двигателя по вертикали
# def move_y(center_x, center_y, obj_center_x, obj_center_y, x1, y1, x2, y2):
#     # while True:

#         print("move_y")  
#         print("center_x", center_x, "center_y", center_y, "obj_center_x", obj_center_x, "obj_center_y", obj_center_y, "x1", x1, "y1", y1, "x2", x2, "y2", y2) 
#         if center_y < y1:
#             move_down()
#         elif center_y > y1 and center_y < obj_center_y:
#             move_down_low()
#         if center_y > y2:
#             move_up()
#         elif center_y < y2 and center_y > obj_center_y:
#             move_up_low()
#         elif center_y == obj_center_y:
#             stop_y()


# функция запуска двигателя по горзонтали
def move_x(): 
    while True:

        sleep(1)

        center_x = state.center_x
        center_y = state.center_y
        obj_center_x = state.obj_center_x
        obj_center_y = state.obj_center_y
        x1 = state.x1
        y1 = state.y1
        x2 = state.x2
        y2 = state.y2


        print("move_x")   
        print("center_x", center_x, "center_y", center_y, "obj_center_x", obj_center_x, "obj_center_y", obj_center_y, "x1", x1, "y1", y1, "x2", x2, "y2", y2)
        if center_x < x1:
            move_right()
        elif center_x > x1 and center_x < obj_center_x:
            move_right_low()
        if center_x > x2:
            move_left()
        elif center_x < x2 and center_x > obj_center_x:
            move_left_low()
        elif center_x == obj_center_x:
            stop_x()
    
# функция запуска двигателя по вертикали
def move_y(center_x, center_y, obj_center_x, obj_center_y, x1, y1, x2, y2):
    # while True:

        print("move_y")  
        print("center_x", center_x, "center_y", center_y, "obj_center_x", obj_center_x, "obj_center_y", obj_center_y, "x1", x1, "y1", y1, "x2", x2, "y2", y2) 
        if center_y < y1:
            move_down()
        elif center_y > y1 and center_y < obj_center_y:
            move_down_low()
        if center_y > y2:
            move_up()
        elif center_y < y2 and center_y > obj_center_y:
            move_up_low()
        elif center_y == obj_center_y:
            stop_y()



