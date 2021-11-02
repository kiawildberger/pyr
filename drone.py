from djitellopy import Tello
from time import sleep
feet = 30
speed = 0.5 # percentage of max
fps = (112/30.4)*speed # feet per second, at speed

tello = Tello()
tello.connect()
tello.takeoff()
tello.send_rc_control(0, speed*100, 0, 0)
sleep(10/fps)
tello.send_rc_control(-speed*100, 0, 0, 0)
sleep(10/fps)
tello.send_rc_control(0, -speed*100, 0, 0)
sleep(10/fps)
tello.send_rc_control(speed*100, 0, 0, 0)

tello.land()