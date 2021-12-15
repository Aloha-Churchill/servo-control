"""Simulating FCFS Disk Scheduling Algorithm on Servo Motor"""

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


def fcfs(l, start):
	accessed_arr = [start]

	sum = 0
	sum += abs(l[0]-start)
	accessed_arr.append(l[0])

	for i in range(1, len(l)):
		sum += abs(l[i] - l[i-1])
		accessed_arr.append(l[i])

	return accessed_arr


l = [2069, 1212,2296,2800,544,1618,356,1523,4965,3681]
increasing_direction = True
max_cylinder = 4999
start = 2000


def convert_to_angle(n):
    r1 = max_cylinder  
    r2 = 180
    return int((n * r2) / r1)

disk_pos_angles = [convert_to_angle(x) for x in l]
angle_start = convert_to_angle(start)
move_positions = fcfs(disk_pos_angles, angle_start)



sg92r_tower_pro = servoMotor()

for pos in move_positions:
    sg92r_tower_pro.set_angle(pos)
    sleep(1)





    

    






