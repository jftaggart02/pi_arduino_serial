import serial
import threading
from time import sleep

# begin serial communication with arduino
ser = serial.Serial('COM6', 9600)

class Motor:
    # STATIC MEMBER VARIABLES -------------------------------------------------
    motor_slew_delay = 0.05 # units are in seconds
    motor_count = 0

    # constructor
    def __init__(self, ser_ID, ser):
        # PRIVATE MEMBER VARIABLES ------------------------------------------------
        self.__ID = Motor.motor_count
        Motor.motor_count += 1
        self.__ser_ID = ser_ID # initialize motor ID we send over serial
        self.ser = ser # pass reference to serial object
        self.__speed = 64 # default speed is stopped (64)
        self.__desired_speed = 64
        self.__slew = False # slew is off by default
        self.__stop_slew = threading.Event() # false by default, when set to true, it stops the slew thread
        

    # PRIVATE MEMBER FUNCTIONS ------------------------------------------------
    def __sendSpeed(self): # sends motor speed attribute to arduino
        # send motor ID to arduino
        self.ser.write(self.__ser_ID)

        # send motor speed to arduino
        self.ser.write(self.__speed.to_bytes(length=1, byteorder='big'))

    def __slew_function(self):
        while self.__stop_slew.is_set() == False:
            # slew functionality
            if self.__desired_speed < self.__speed:
                self.__speed += 1
                self.__sendSpeed()
            elif self.__desired_speed > self.__speed:
                self.__speed += 1
                self.__sendSpeed()
            sleep(Motor.motor_slew_delay)

    # PUBLIC MEMBER FUNCTIONS -------------------------------------------------
    def setSpeed(self, speed_to_set): # sets motor speed attribute
        # constrain motor speed to value from 0 to 128
        if speed_to_set < 0:
            speed_to_set = 0
        if speed_to_set > 128:
            speed_to_set = 128

        # if slew is not on, send speed to arduino manually
        if self.__slew == False:
            self.__speed = speed_to_set
            self.__sendSpeed()

        # if slew is on, set desired speed
        elif self.__slew == True:
            self.__desired_speed = speed_to_set

    def setSlew(self, slew_bool):
        if slew_bool == True:
            self.__slew_thread = threading.Thread(target=self.__slew_function, args=(self.__ID,), daemon=True)
            self.__slew_thread.start()
        elif slew_bool == False:
            self.__stop_slew.set()

# waits for arduino to indicate that it's ready
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

# -------------------------------------
# Here's the main part of the program:
# -------------------------------------

if __name__ == "__main__":

    # wait for arduino to be ready to receive data
    wait_for_arduino()

    motor_right.setSlew(True)

    motor_right.setSpeed(128)
    sleep(5)
    motor_right.setSpeed(64)
    sleep(5)