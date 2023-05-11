# import serial library
import serial
from time import sleep

# begin serial communication at baud of 9600
# run ls dev/tty* and see if there's an "ACMX" or "USBX"
# and change the serial address below accordingly.
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        # slowly increase LED values
        for x in range(0, 200, 20):
            ser.write(1)
            ser.write(x)
            ser.write(2)
            ser.write(x)
            sleep(1)
        # slowoy decrease LED values
        for x in range(200, 0, -20):
            ser.write(1)
            ser.write(x)
            ser.write(2)
            ser.write(x)
            sleep(1)

