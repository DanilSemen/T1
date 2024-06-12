import keyboard
# from vision.state import state
from motor.shot import *
from motor.motor3 import motor1, motor2
from vision.state import state
# from shot import *

def wait_for_key():
    print("Ожидание нажатия клавиши...")

    while True:
        # Ожидаем нажатие клавиши "пробел" или "A"
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:  # Проверка на событие нажатия клавиши
            if event.name == 'space':
                print("стоп")
                motor1.stop()
                motor2.stop()
                print(state.center_x, state.center_y, state.obj_center_x, state.obj_center_y, state.x1, state.y1, state.x2, state.y2)
             
            elif event.name == 'a':
                print("@shot@")
                shot()
            elif event.name == 's':
                print("@shot@")
                wshot()
            elif event.name == 'left':
                print("влево")
                motor1.stop()
                motor1.start_moving(direction=1)

            elif event.name == 'right':
                print("вправо")
                motor1.stop()
                motor1.start_moving(direction=0)


            elif event.name == 'up':
                print("вверх")
                motor2.stop()
                motor2.start_moving(direction=0)
            elif event.name == 'down':
                print("вниз")
                motor2.stop()
                motor2.start_moving(direction=1)

                    

if __name__ == "__main__":
    # from motor.motor3 import *
    from shot import *
    from motor3 import motor1, motor2
    from motor3 import *
    wait_for_key()

    




