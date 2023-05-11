# import serial library
import serial
from time import sleep

delay = 0.01
waiting = True

# begin serial communication at baud of 9600
# run ls dev/tty* and see if there's an "ACMX" or "USBX"
# and change the serial address below accordingly.
if __name__ == '__main__':
    ser = serial.Serial('COM6', 9600)
    ser.reset_input_buffer()
    
    print("Waiting...")
    
    while waiting == True:
        if ser.in_waiting > 0:
            print("Received something.")
            char = ser.read(1).decode('utf-8')
            if char == '1':
                print("Arduino is ready.")
                waiting = False
                
    print("Done waiting.")
  
    while True:
        # slowly increase LED values
        for x in range(0, 256, 2):
            ser.write(b'1')
            ser.write(x.to_bytes())
            ser.write(b'2')
            ser.write(x.to_bytes())
            sleep(delay)
        # slowoy decrease LED values
        for x in range(255, 0, -2):
            ser.write(b'1')
            ser.write(x.to_bytes())
            ser.write(b'2')
            ser.write(x.to_bytes())
            sleep(delay)

