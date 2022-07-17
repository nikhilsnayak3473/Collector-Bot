import time
import sys
from videocapture import VideoCapture
import RPi.GPIO as GPIO
from motor_driver import L298N, MG996R
from tomato_detector import TomatoDetector


# General Configuration
robot_speed = 55
thershold_distance = 30

#Tomato Types
RED_TOMATO = 'RED'
YELLOW_TOMATO = 'YELLOW'

# GPIO Configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor Driver Pins
ENA = 26
IN1 = 19
IN2 = 13
IN3 = 16
IN4 = 20
ENB = 21

# Arm Servo Channels
base_servo_channel = 0
s1_servo_channel = 1
s2_servo_channel = 2
s3_servo_channel = 3
gripper_servo_channel = 4

# Static values for arm position
base_servo_init = 0
base_servo_basket_red = 125
base_servo_basket_yellow = 90
s1_servo_init = 10
s1_servo_basket = 10
s2_servo_init = 90
s2_servo_basket = 150
s3_servo_init = 170
s3_servo_basket = 150
gripper_servo_init = 100
gripper_servo_grip = 50

def set_arm_init():
    print("arm moving to initial position...")
    s1_servo.setangle(s1_servo_init)
    s2_servo.setangle(s2_servo_init)
    s3_servo.setangle(s3_servo_init)
    base_servo.setangle(base_servo_init)
    time.sleep(1)
    print("done..")


def set_arm_basket(TOMATO_TYPE):
    print(f'arm moving to {TOMATO_TYPE} basket   ')
    s1_servo.setangle(s1_servo_init+5)
    s2_servo.setangle(s2_servo_init+23)
    gripper_servo.setangle(gripper_servo_grip)
    if TOMATO_TYPE == RED_TOMATO:
        base_servo.setangle(base_servo_basket_red)
    elif TOMATO_TYPE == YELLOW_TOMATO:
        base_servo.setangle(base_servo_basket_yellow)
    s3_servo.setangle(s3_servo_basket)
    gripper_servo.setangle(gripper_servo_init)
    time.sleep(1)
    print('done..')


def main():
    print("----------------main-----------------")
    while True:
        img = camera.read()
        red_distance = red_tomato.get_distance(img)
        yellow_distance = yellow_tomato.get_distance(img)

        if (red_distance != None) and (red_distance < thershold_distance):
            print('red tomato detected')
            motor_controller.stop()
            set_arm_basket(RED_TOMATO)
            set_arm_init()
        elif (yellow_distance != None) and (yellow_distance < thershold_distance):
            print('yellow tomato detected')
            motor_controller.stop()
            set_arm_basket(YELLOW_TOMATO)
            set_arm_init()
        else:
            motor_controller.backward(robot_speed)


def test():
    print("-------test---------")
    #gripper_servo.setangle(gripper_servo_grip)
    #base_servo.setangle(base_servo_basket_red)
    #s1_servo.setangle(s1_servo_basket+20)
    s2_servo.setangle(s2_servo_basket)
    #s3_servo.setangle(s3_servo_basket)
    #s3_servo.setangle(s3_servo_init)
    s2_servo.setangle(s2_servo_init)
    #s1_servo.setangle(s1_servo_init)
    #base_servo.setangle(base_servo_init)
    #gripper_servo.setangle(gripper_servo_init)


if __name__ == '__main__':
    try:
        # Instantiation of Controllers
        motor_controller = L298N(ENA, IN1, IN2, IN3, IN4, ENB)
        red_tomato = TomatoDetector(RED_TOMATO)
        yellow_tomato = TomatoDetector(YELLOW_TOMATO)
        camera = VideoCapture(0)
        base_servo = MG996R(base_servo_channel, base_servo_init)
        s1_servo = MG996R(s1_servo_channel, s1_servo_init)
        s2_servo = MG996R(s2_servo_channel, s2_servo_init)
        s3_servo = MG996R(s3_servo_channel, s3_servo_init)
        gripper_servo = MG996R(gripper_servo_channel, gripper_servo_init)

        main()
        #test()
    except Exception as e:
        print(e)
    finally:
        print("exiting...")
        GPIO.cleanup()
        camera.release()
        sys.exit()
