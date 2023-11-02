from Motor import Motor
from Motor import wait_for_arduino
import serial
from time import sleep

if __name__ == "__main__":

    # begin serial communication with arduino
    ser = serial.Serial('COM11', 9600)

    # wait for arduino to be ready to receive data
    wait_for_arduino(ser)

    motor_right = Motor(b"r", ser)
    motor_left = Motor(b"l", ser)

    motor_right.setSlew(True)
    motor_left.setSlew(True)

    motor_right.setSlewRate(1)
    motor_left.setSlewRate(1)

    motor_right.setSpeed(128)
    motor_left.setSpeed(0)
    sleep(3)
    
    motor_right.setSpeed(64)
    motor_left.setSpeed(64)
    sleep(3)

    motor_right.setSlew(False)
    motor_left.setSlew(False)
    
    motor_right.setSpeed(128)
    motor_left.setSpeed(0)
    sleep(3)
    
    motor_right.setSpeed(64)
    motor_left.setSpeed(64)
    sleep(3)

    # Let's try this again:

    motor_right.setSlew(True)
    motor_left.setSlew(True)

    motor_right.setSlewRate(1)
    motor_left.setSlewRate(1)

    motor_right.setSpeed(128)
    motor_left.setSpeed(0)
    sleep(3)
    
    motor_right.setSpeed(64)
    motor_left.setSpeed(64)
    sleep(3)

    motor_right.setSlew(False)
    motor_left.setSlew(False)
    
    motor_right.setSpeed(128)
    motor_left.setSpeed(0)
    sleep(3)
    
    motor_right.setSpeed(64)
    motor_left.setSpeed(64)
    sleep(3)