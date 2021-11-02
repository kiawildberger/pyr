from djitellopy import Tello
from time import sleep
feet = 30
speed = 0.5 # percentage of max
fps = (224/30.4)*(1/speed) # feet per second, at speed
vfps = (52/30.4)*(1/speed)

tello = Tello()
tello.connect()
tello.takeoff()
nspeed = speed*100

tello.send_rc_control(0, 0, nspeed, 0) # scoot another 3ft up
sleep(3/vfps)

tello.send_rc_control(0, nspeed, 0, 0)
sleep(10/fps)
tello.send_rc_control(-nspeed, 0, 0, 0)
sleep(10/fps)
tello.send_rc_control(0, -nspeed, 0, 0)
sleep(10/fps)
tello.send_rc_control(nspeed, 0, 0, 0)

tello.land()