from djitellopy import tello
import KeyPress as kp
import numpy as np
from time import sleep
import cv2, math

### parameters

fSpeed = 117/10 # forward speed in cm 150/s
aSpeed = 360/10 # angular speed deg/s
interval = 0.25


dInterval = fSpeed * interval
aInterval = aSpeed * interval

kp.init()
tello = tello.Tello()
tello.connect()
print(f'battery at {tello.get_battery()}')

def get_keyboard_input():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"):yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): yv = tello.land()
    if kp.getKey("e"): yv = tello.takeoff()

    return [lr, fb, ud, yv]

def draw_points();
    cv2.circle(img,(300,500))

while True:
    vals = get_keyboard_input()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    draw_points()
