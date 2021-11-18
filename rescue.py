from djitellopy import Tello
import time, math

tello = Tello()
tello.connect()

distance = (0, 0) # ew, ns
feet = 30.48

def f(d):
    return round(feet*d)

tello.takeoff()

tello.move_up(f(6))
time.sleep(2)

tello.send_rc_control(0, 0, 0, 50) # now facing east
time.sleep(3.46)
tello.move_forward(f(5))
time.sleep(2)

tello.send_rc_control(0, 0, 0, -50) # turn back north
time.sleep(3.46)
tello.move_forward(f(6))
time.sleep(2)

tello.send_rc_control(0, 0, 0, 50) # east again
time.sleep(3.46)
tello.move_down(f(3))
time.sleep(2)
tello.move_forward(f(3))
time.sleep(2)

tello.send_rc_control(0, 0, 0, 50) # south
time.sleep(3.46)
tello.move_forward(f(3))
time.sleep(2)

tello.send_rc_control(0, 0, 0, -50) # east
time.sleep(3.46)
tello.move_forward(f(6))
time.sleep(2)

tello.land()
