"""Module to control hobbyist servo motors using MicroPython"""

from machine import Pin, PWM
from time import sleep

RP_MAX_DUTY = 65535

class servoMotor:

    def __init__(self, pin=0, freq=50):
        self.pin = pin
        self.freq = freq
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)

    def set_frequency(self, new_freq):
        self.freq = new_freq
        self.pwm.freq(new_freq)
    
    def set_angle(self, angle):
        if angle<0 or angle>180:
            print("Angle is out of bounds")
        else:
            self.pwm.duty_u16(angle_to_duty(angle))

    
    def move_from_to(self, old_angle, new_angle, speed=0):
        if speed < 0 or speed > 100:
            print("Speed needs to be from range 0-100")

        elif new_angle < 0 or new_angle > 180 or old_angle < 0 or old_angle > 180:
            print("Angle is out of bounds")

        else:
            self.pwm.duty_u16(angle_to_duty(old_angle))
            curr_pos = angle_to_duty(old_angle)
            desired_pos = angle_to_duty(new_angle)
            while abs(curr_pos - desired_pos) > 0:
                new_pos = curr_pos + 1
                self.pwm.duty_u16(new_pos)
                curr_pos = new_pos
                sleep(0.0001*(100-speed))



def angle_to_duty(theta):
    a = ((theta*1.0) /180.0) + 1
    val = int(a*RP_MAX_DUTY/20.0)
    return val



sg92r_tower_pro = servoMotor()
sg92r_tower_pro.set_angle(180)
sg92r_tower_pro.move_from_to(0, 90, speed=0)
print(angle_to_duty(63))





    

    
