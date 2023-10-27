import serial
from time import sleep

ser = serial.Serial('COM6', 9600)

class Motor:
    def __init__(self, ID, ser):
        # initialize motor ID
        self.ID = ID
        # pass reference to serial object
        self.ser = ser

    def setSpeed(self, speed):
        # send motor ID to arduino
        self.ser.write(self.ID)

        # constrain motor speed to value from 0 to 100
        if speed < 0:
            speed = 0
        if speed > 128:
            speed = 128

        # send motor speed to arduino
        self.ser.write(speed.to_bytes(length=1, byteorder='big'))

def wait_for_arduino():

    # waits to receive this character
    arduino_ready_signal = 'R'
    
    waiting = True
    
    print("Waiting...")

    while waiting:
        if ser.in_waiting > 0:
            char = ser.read(1).decode('utf-8')
            if char == arduino_ready_signal:
                print("Arduino is ready.")
                waiting = False
                
    print("Done waiting.")

motor_right = Motor(b"r", ser)
motor_left = Motor(b"l", ser)

wait_for_arduino()

while True:
    for x in range(64, 128):
        speed = x
        motor_right.setSpeed(speed)
        motor_left.setSpeed(speed)
        sleep(0.020)
    
    for x in range(128, 64):
        speed = x
        motor_right.setSpeed(speed)
        motor_left.setSpeed(speed)
        sleep(0.020)