# PROGRAM FUNCTION: Send serial messages to arduino that control the
# brightness of 2 different LEDs

# import serial library
import serial
from time import sleep

delay = 0.01

# begin serial communication at baud of 9600
# run ls dev/tty* and see if there's an "ACMX" or "USBX"
# and change the serial address below accordingly.
if __name__ == '__main__':
    ser = serial.Serial('COM6', 9600)
    ser.reset_input_buffer()
    
    print("Waiting...")
    
    waiting = True
    
    # wait to receive message from Arduino indicating it's ready
    while waiting:
        if ser.in_waiting > 0:
            char = ser.read(1).decode('utf-8')
            if char == 'R':
                print("Arduino is ready.")
                waiting = False
                
    print("Done waiting.")
  
    while True:
        # slowly increase LED brightness
        for x in range(0, 256, 2):
            ser.write(b'1')
            ser.write(x.to_bytes())
            ser.write(b'2')
            ser.write(x.to_bytes())
            sleep(delay)
        # slowly decrease LED brightness
        for x in range(255, 0, -2):
            ser.write(b'1')
            ser.write(x.to_bytes())
            ser.write(b'2')
            ser.write(x.to_bytes())
            sleep(delay)

