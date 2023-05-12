# PROGRAM FUNCTION: Reads bytes from arduino and sends them back one by one

# import serial library
import serial

# begin serial communication at baud of 9600
# run ls dev/tty* and see if there's an "ACMX" or "USBX"
# and change the serial address below accordingly.
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        # wait for byte to appear in input buffer
        if ser.in_waiting > 0:
            # read 1 byte
            val = ser.read(1)
            # send value to arduino
            ser.write(val)
