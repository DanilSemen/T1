import wiringpi
from wiringpi import GPIO
from time import sleep
from threading import Thread

wiringpi.wiringPiSetup() 


class StepperMotor:
    def __init__(self, direction_pin, pulse_pin):
        wiringpi.pinMode(direction_pin, GPIO.OUTPUT)
        wiringpi.pinMode(pulse_pin, GPIO.OUTPUT)
        
        self.direction_pin = direction_pin
        self.pulse_pin = pulse_pin
        self.speed = 0 #1000
        self.speed_low = 10
        self.acceleration = 0
        self.deceleration = 0
        self.running = False

    def set_speed(self, max_speed):
        self.speed = max_speed
    
    def _motor_loop(self, direction):
        wiringpi.digitalWrite(self.direction_pin, direction)
        while self.running:
            wiringpi.digitalWrite(self.pulse_pin, 1)
            sleep(1 / self.speed)
            wiringpi.digitalWrite(self.pulse_pin, 0)
            sleep(1 / self.speed)

    def start_moving(self, direction):
            if not self.running:
                self.running = True
                self.thread = Thread(target=self._motor_loop, args=(direction,))
                self.thread.start()

    def _motor_loop_low(self, direction):
        wiringpi.digitalWrite(self.direction_pin, direction)
        while self.running:
            wiringpi.digitalWrite(self.pulse_pin, 1)
            sleep(1 / self.speed_low)
            wiringpi.digitalWrite(self.pulse_pin, 0)
            sleep(1 / self.speed_low)
    
    def start_moving_low(self, direction):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self._motor_loop_low, args=(direction,))
            self.thread.start()

    def stop1(self):
        self.running = False
        if self.thread:
            self.thread.join()
    
    def stop(self):
        self.running = False


    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

    def set_deceleration(self, deceleration):
        self.deceleration = deceleration

    def step_motor(self, direction, steps, initial_speed): #def step_motor(self, direction, steps, initial_speed=0):
        wiringpi.digitalWrite(self.direction_pin, direction)
        
        current_speed = initial_speed
        
        for _ in range(steps):
            wiringpi.digitalWrite(self.pulse_pin, 1)
            sleep(1/self.speed)
            wiringpi.digitalWrite(self.pulse_pin, 0)
            
            if current_speed < self.speed:  # Увеличиваем скорость до максимальной
                current_speed += self.acceleration
                if current_speed > self.speed:
                    current_speed = self.speed
            elif current_speed > self.speed:  # Уменьшаем скорость до максимальной
                current_speed -= self.deceleration
                if current_speed < self.speed:
                    current_speed = self.speed
            # print(current_speed, self.speed, self.acceleration )
            sleep(1 / current_speed)  # Добавили деление на 1000, чтобы скорость была в секундах
            # sleep(current_speed)  # Добавили деление на 1000, чтобы скорость была в секундах

# Создаем экземпляры класса StepperMotor для двух двигателей
motor1 = StepperMotor(2, 0)
motor2 = StepperMotor(11, 8)

# горизонтальный двигатель

motor1.set_speed(100)
motor1.set_acceleration(100)
motor1.set_deceleration(100)

# вертикальный двигатель

motor2.set_speed(20000) # 10500
motor2.set_acceleration(4500)
motor2.set_deceleration(0)




# motor1.start_moving(direction=1)
# sleep(1)
# motor1.stop()