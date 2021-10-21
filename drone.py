from djitellopy import Tello
tello = Tello()
tello.connect()
tello.takeoff()
tello.move_forward(100) # centimeters
tello.land()