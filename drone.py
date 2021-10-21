from djitellopy import Tello
feet = 30

tello = Tello()
tello.connect()
tello.takeoff()
tello.move_forward(10*feet)
tello.move_left(10*feet)
tello.move_back(10*feet)
tello.move_right(10*feet)
tello.land()