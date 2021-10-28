from djitellopy import Tello
from time import sleep
feet = 30
fps = 2 # feet per second

tello = Tello()
tello.connect()
tello.takeoff()
tello.send_rc_control(0, 50, 0, 0)
sleep(10/fps)
tello.send_rc_control(-50, 0, 0, 0)
sleep(10/fps)
tello.send_rc_control(0, -50, 0, 0)
sleep(10/fps)
tello.send_rc_control(50, 0, 0, 0)

tello.land()