from machine import Pin, PWM
from time import sleep




RP_MAX_DUTY = 65535

pwm = PWM(Pin(0))
pwm.freq(50)


"""
Angle 0 - 180 degrees
Needs to be turned into duty cycle
0 = 1/20
90 = 1.5/20
180 = 2/20
RP2040 max duty cycle = 65535

"""

def angle_to_duty(theta):
    if theta<0 or theta>180:
        print("Angle is out of bounds")
    else:
        duty = int(theta*RP_MAX_DUTY/1800)
        print("Duty cycle is: " + str(duty))
        return duty
"""
pwm.duty_u16(angle_to_duty(0))
sleep(1)
pwm.duty_u16(angle_to_duty(90))
sleep(1)
pwm.duty_u16(angle_to_duty(120))
sleep(1)
pwm.duty_u16(angle_to_duty(180))

calc time that it takes to swing around
choose rotation time
we want to build library that initializes object
"""
curr_pos = 2000
desired_pos = 3000
while abs(curr_pos - desired_pos) > 0:
    pwm.duty_u16(curr_pos + 10)
    curr_pos += 10
    sleep(0.1)



    

    
