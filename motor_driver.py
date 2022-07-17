from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import time


class TB6612FNG:
    def __init__(self, PWMA, AIN1, AIN2, PWMB, BIN1, BIN2, STDBY):
        self.PWMA = PWMA
        self.AIN1 = AIN1
        self.AIN2 = AIN2
        self.PWMB = PWMB
        self.BIN1 = BIN1
        self.BIN2 = BIN2
        self.STDBY = STDBY
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.AIN1, GPIO.OUT)
        GPIO.setup(self.AIN2, GPIO.OUT)
        GPIO.setup(self.PWMB, GPIO.OUT)
        GPIO.setup(self.BIN1, GPIO.OUT)
        GPIO.setup(self.BIN2, GPIO.OUT)
        GPIO.setup(self.STDBY, GPIO.OUT)
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.LOW)
        GPIO.output(self.STDBY, GPIO.HIGH)
        self.pwma = GPIO.PWM(self.PWMA, 100)
        self.pwmb = GPIO.PWM(self.PWMB, 100)
        self.pwma.start(25)
        self.pwmb.start(25)

    def forward(self, speed=25):
        GPIO.output(self.AIN1, GPIO.HIGH)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.HIGH)
        GPIO.output(self.BIN2, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwma.ChangeDutyCycle(speed)
        self.pwmb.ChangeDutyCycle(speed)

    def backward(self, speed=25):
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.HIGH)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.HIGH)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwma.ChangeDutyCycle(speed)
        self.pwmb.ChangeDutyCycle(speed)

    def softleftforward(self, speed=25):
        GPIO.output(self.AIN1, GPIO.HIGH)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwma.ChangeDutyCycle(speed)

    def softleftbackward(self, speed=25):
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.HIGH)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwma.ChangeDutyCycle(speed)

    def softrightforward(self, speed=25):
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.HIGH)
        GPIO.output(self.BIN2, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwmb.ChangeDutyCycle(speed)

    def softrightbackward(self, speed=25):
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.HIGH)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwmb.ChangeDutyCycle(speed)

    def hardleft(self, speed=25):
        GPIO.output(self.AIN1, GPIO.HIGH)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.HIGH)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwma.ChangeDutyCycle(speed)
        self.pwmb.ChangeDutyCycle(speed)

    def hardright(self, speed=25):
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.HIGH)
        GPIO.output(self.BIN1, GPIO.HIGH)
        GPIO.output(self.BIN2, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.pwma.ChangeDutyCycle(speed)
        self.pwmb.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.LOW)


class L298N:
    def __init__(self, ENA, IN1, IN2, IN3, IN4, ENB):
        self.ENA = ENA
        self.IN1 = IN1
        self.IN2 = IN2
        self.ENB = ENB
        self.IN3 = IN3
        self.IN4 = IN4
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.ENA = GPIO.PWM(self.ENA, 100)
        self.ENB = GPIO.PWM(self.ENB, 100)
        self.ENA.start(25)
        self.ENB.start(25)

    def forward(self, speed=25):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed+30)

    def backward(self, speed=25):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed+10)

    def softleftforward(self, speed=25):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENA.ChangeDutyCycle(speed)

    def softleftbackward(self, speed=25):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENA.ChangeDutyCycle(speed)

    def softrightforward(self, speed=25):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENB.ChangeDutyCycle(speed)

    def softrightbackward(self, speed=25):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENB.ChangeDutyCycle(speed)

    def hardleft(self, speed=25):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed)

    def hardright(self, speed=25):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        if speed > 90:
            speed = 90
        elif speed < 0:
            speed = 0
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)


class SG90:
    def __init__(self, pin, initial_pose):
        self.servo = pin
        GPIO.setup(self.servo, GPIO.OUT)
        self.angleControl = GPIO.PWM(self.servo, 50)
        self.angleControl.start((initial_pose / 18.0) + 2.5)
        self.current_angle = initial_pose
        time.sleep(0.5)

    def setangle(self, angle):
        if(self.current_angle < angle):
            while(self.current_angle <= angle):
                duty = (self.current_angle / 18.0) + 2
                self.angleControl.ChangeDutyCycle(duty)
                time.sleep(0.1)
                self.current_angle = self.current_angle + 1

        else:
            while(self.current_angle >= angle):
                duty = (self.current_angle / 18.0) + 2
                self.angleControl.ChangeDutyCycle(duty)
                time.sleep(0.1)
                self.current_angle = self.current_angle - 1

        self.current_angle = angle


class MG996R():
    def __init__(self, channel, initial_pose):
        kit = ServoKit(channels = 16)
        self.servo = kit.servo[channel]
        self.servo.angle = initial_pose
        self.current_angle = initial_pose
        time.sleep(1)

    def setangle(self,angle):
        if(self.current_angle <angle):
            while(self.current_angle <= angle):
                self.servo.angle = self.current_angle
                time.sleep(0.1)
                self.current_angle+=1
        else:
            while(self.current_angle >= angle):
                self.servo.angle = self.current_angle
                time.sleep(0.1)
                self.current_angle -= 1

        self.current_angle = angle


