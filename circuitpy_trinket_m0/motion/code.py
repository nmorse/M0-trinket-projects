import board
import time
import pulseio
pwm = pulseio.PWMOut(board.D0, frequency=50)
import adafruit_motor.servo
servo = adafruit_motor.servo.Servo(pwm)

time.sleep(1.0)
a = 0
dir = 'up'
servo.angle = 20

while True:
    time.sleep(0.02)
    if a >= 180:
        dir = 'down'
        time.sleep(0.5)
    if a <= 0:
        dir = 'up'
        time.sleep(0.5)

    if dir == 'up':
        a += 5
    else:
        a -= 5

    servo.angle = a
