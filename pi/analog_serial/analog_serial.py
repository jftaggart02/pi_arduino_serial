# import serial library
import serial

# begin serial communication at baud of 9600
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        # wait for byte to appear in input buffer
        if ser.in_waiting > 0:
            # read 1 byte
            analog_val = ser.read(1)
            # print "I read " + value
            print("I read ")
            print(analog_val)
