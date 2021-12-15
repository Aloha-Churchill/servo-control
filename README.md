# Servo Controller

This is a simple micropython class to help with controlling servo motors. The function, ```angle_to_duty(theta) ``` translates a user defined angle from 0-180 to the corresponding number that a Raspberry Pi Pico can interpret as a duty cycle. Then, the PWM library is used to send the correct PWM to the Raspberry Pi via a user defined pin.


### Disk Scheduling on the Servo Controller
In the example, there is a mini demonstration of this class in use. It takes in a list and somewhat simulates the first come first serve (FCFS) disk scheduling algorithm.
