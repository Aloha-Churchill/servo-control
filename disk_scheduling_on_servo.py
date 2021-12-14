import disk_scheduling as ds
import servo as s
from time import sleep

servo1 = s.servoMotor()

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
max_cylinder_angle = convert_to_angle(start)

move_positions = ds.fcfs(disk_pos_angles, angle_start)

for pos in move_positions:
    servo1.set_angle(pos)
    sleep(0.1)

