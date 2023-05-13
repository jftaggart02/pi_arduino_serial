# PROGRAM FUNCTION: arduino sends 2 analog values to raspberry pi, gets them back, and lights up each LED with their respective value

# import serial library
import serial
from time import sleep

# begin serial communication at baud of 9600
# on raspberry pi:
#   run ls dev/tty* and see if there's an "ACMX" or "USBX"
#   and change the serial address below accordingly.
ser = serial.Serial('COM6', 9600, timeout=1)
ser.reset_input_buffer()

arduino_ready_signal = 'R'

waiting = True

print("Waiting...")

# waits for the arduino to send a character indicating that it's ready to transmit data
while waiting:
    if ser.in_waiting > 0:
        char = ser.read(1).decode('utf-8')
        if char == arduino_ready_signal:
            print("Arduino is ready.")
            waiting = False
            
print("Done waiting.")

# sends message to arduino saying, "I'm ready to receive data!"
ser.write(b'R')

while True:
    # wait for at least 3 bytes to be in input buffer
    if ser.in_waiting >= 3:
        
        # read 3 bytes
        # the first 2 are the potentiometer ID
        # the third one is the potentiometer value (0 to 255)
        potID = ser.read(2).decode('utf-8')
        potVal = ser.read(1)
        
        # if we read the ID of potentiometer 1,
        if potID == 'P1':
            # send back LED1's ID
            ser.write(b'L1')
            
        # if we read the ID of potentiometer 2,
        if potID == 'P2':
            # send back LED2's ID
            ser.write(b'L2')
            
        # send back the value received
        ser.write(potVal)