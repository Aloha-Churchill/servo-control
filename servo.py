"""Module to control hobbyist servo motors"""

from machine import Pin, PWM
from time import sleep

RP_MAX_DUTY = 65535

class servoMotor:

    def __init__(self, pin=0, freq=50):
        self.pin = pin
        self.freq = freq
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.pwm.duty_u16(angle_to_duty(0))
        self.angle = 0

    def set_frequency(self, new_freq):
        self.freq = new_freq
        self.pwm.freq(new_freq)
    
    def set_angle(self, angle):
        if angle<0 or angle>180:
            print("Angle is out of bounds")
        else:
            self.pwm.duty_u16(angle_to_duty(angle))

    def move_to(self, new_angle, speed=0):
        if speed < 0 or speed > 100:
            print("Speed needs to be from range 0-100")

        elif new_angle < 0 or new_angle > 180:
            print("Angle is out of bounds")

        else:
            curr_pos = self.angle
            desired_pos = angle_to_duty(new_angle)
            while abs(curr_pos - desired_pos) > 0:
                new_pos = curr_pos + 1
                self.pwm.duty_u16(new_pos)
                curr_pos = new_pos
                sleep(0.01*speed)



def angle_to_duty(theta):
    duty = int(theta*RP_MAX_DUTY/1800)
    print("Duty cycle is: " + str(duty))
    return duty      





    

    
