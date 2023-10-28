import serial
import threading
from time import sleep


class Motor:
    # NOTES -------------------------------------------------------------------
        # Motor speed ranges from 0 (full reverse) to 64 (stopped) to 128 (full forward) 

    # USAGE ------------------------------------------------------------------
        # Example: 
            # Initialize serial connection with arduino:
            # ser = serial.Serial('COM6', 9600)

            # Instantiate two Motor objects using char ID and serial object
            # motor_right = Motor(b"r", ser)
            # motor_left = Motor(b"l", ser)
            
            # Enable motor slew rate
            # motor_right.setSlew(True)
            # motor_left.setSlew(True)

            # Run right motor full forwards and left motor full backwards for 5 seconds
            # motor_right.setSpeed(128)
            # motor_left.setSpeed(0)
            # sleep(5)

            # Stop motors
            # motor_right.setSpeed(64)
            # motor_left.setSpeed(64)


    # STATIC CLASS VARIABLES --------------------------------------------------
    motor_slew_time = 3 # time (seconds) it takes for motors to spin from stopped to full speed
    motor_slew_delay = motor_slew_time / 64
    motor_count = 0


    # constructor
    def __init__(self, ser_ID, ser):
        # PRIVATE MEMBER VARIABLES --------------------------------------------
        self.__ID = Motor.motor_count
        Motor.motor_count += 1

        self.__ser_ID = ser_ID # sets motor ID char that gets sent over serial
        self.__ser = ser # get reference to serial object

        # default speed is stopped (64)
        self.__speed = 64 # speed that gets sent to arduino every time self.__sendSpeed() is called
        self.__desired_speed = 64 # desired speed that we increment self.__speed towards when motor slew is enabled

        self.__slew = False # slew is disabled by default
        self.__stop_slew = threading.Event() # false by default, when set to true, it stops the slew thread
        

    # PRIVATE MEMBER FUNCTIONS ------------------------------------------------
    def __sendSpeed(self): # sends motor speed attribute to arduino
        # send motor ID to arduino
        self.__ser.write(self.__ser_ID)

        # send motor speed to arduino
        self.__ser.write(self.__speed.to_bytes(length=1, byteorder='big'))


    def __slew_function(self):
        while self.__stop_slew.is_set() == False:

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


    def setSlewRate(self, slew_time):
        Motor.motor_slew_time = slew_time
        Motor.motor_slew_delay = Motor.motor_slew_time / 64


# waits for arduino to indicate that it's ready
def wait_for_arduino(ser):

    # waits to receive this character
    arduino_ready_signal = 'R'
    
    waiting = True
    
    print("Waiting for Arduino...")

    while waiting:
        if ser.in_waiting > 0:
            char = ser.read(1).decode('utf-8')
            if char == arduino_ready_signal:
                print("Arduino is ready.")
                waiting = False
                
    print("Arduino is ready.")


# -----------------------------------------------------------------------------
# Here's the main part of the program:
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # begin serial communication with arduino
    ser = serial.Serial('COM6', 9600)

    # wait for arduino to be ready to receive data
    wait_for_arduino(ser)

    motor_right = Motor(b"r", ser)
    motor_left = Motor(b"l", ser)

    motor_right.setSlew(True)
    motor_left.setSlew(True)

    motor_right.setSpeed(128)
    motor_left.setSpeed(0)
    sleep(5)
    
    motor_right.setSpeed(64)
    motor_left.setSpeed(64)