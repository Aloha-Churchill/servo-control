import servo as s


sg92r_tower_pro = s.servoMotor()
another_servo = s.servoMotor(1, 100)


another_servo.set_frequency(500)
sg92r_tower_pro.set_angle(100)
sg92r_tower_pro.move_to(180)
sg92r_tower_pro.move_to(0, speed=99)

print(s.angle_to_duty(63))



