# import serial library
import serial

# begin serial communication at baud of 9600
# run ls dev/tty* and see if there's an "ACMX" or "USBX"
# and change the serial address below accordingly.
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        # wait for at least 2 bytes to be in input buffer
        if ser.in_waiting > 1:
            
            # read 2 bytes
            potID = ser.read(1)
            potVal = ser.read(1)
            
            # if the first byte is the number 1,
            if potID == 1:
                # send back the number 3
                ser.write(3)
                
            # if the first byte is the number 2,
            if potID == 2:
                # send back the number 4
                ser.write(4)
                
            # else
            else:
                #send back 0
                ser.write(0)
                
            # send back the value received
            ser.write(potVal)