# import serial library
import serial
from time import sleep


# global variables
color_cycle_delay = 0.01
arduino_ready_signal = 'R'


# begin serial communication at baud of 9600
# run ls dev/tty* and see if there's an "ACMX" or "USBX"
# and change the serial address below accordingly.
ser = serial.Serial('COM6', 9600)

    
# waits for the arduino to send a character indicating
# that it's ready to receive data
def wait_for_arduino():
    global arduino_ready_signal
    waiting = True
    
    print("Waiting...")

    while waiting:
        if ser.in_waiting > 0:
            print("Received something.")
            char = ser.read(1).decode('utf-8')
            if char == arduino_ready_signal:
                print("Arduino is ready.")
                waiting = False
                
    print("Done waiting.")


class RGBLED:
    # initializes LED with unique ID. Must be a single character converted to bytes
    # example: b"1"
    def __init__(self, ID):
        self.ID = ID
    
    # sends serial message to arduino which it uses to 
    # change the color of the RGB LED
    def setColor(self, r, g, b):
        ser.write(self.ID)
        ser.write(r.to_bytes(length=1,byteorder='big'))
        ser.write(g.to_bytes(length=1,byteorder='big'))
        ser.write(b.to_bytes(length=1,byteorder='big'))

    # tells the arduino to make the LED cycle through color spectrum
    def colorCycle(self):
        # transition from red to yellow
        for x in range(256):
            self.setColor(255, x, 0)
            sleep(color_cycle_delay)
        
        # transition to green
        for x in range(255, 0, -1):
            self.setColor(x, 255, 0)
            sleep(color_cycle_delay)
            
        # transition to teal
        for x in range(256):
            self.setColor(0, 255, x)
            sleep(color_cycle_delay)
        
        # transition to blue
        for x in range(255, 0, -1):
            self.setColor(0, x, 255)
            sleep(color_cycle_delay)
        
        # transition to pink
        for x in range(256):
            self.setColor(x, 0, 255)
            sleep(color_cycle_delay)
        
        # transition back to red
        for x in range(255, 0, -1):
            self.setColor(255, 0, x)
            sleep(color_cycle_delay)
   
    def turnOff(self):
        self.setColor(0, 0, 0)


# here I create 2 RGBLED objects
LED1 = RGBLED(b"1")
LED2 = RGBLED(b"2")
        
    
# in case there was anything in the input buffer we didn't want,
# we clear it
ser.reset_input_buffer()


# wait for arduino to be ready
wait_for_arduino()


while True:
    LED1.colorCycle()
    LED1.turnOff()
    LED2.colorCycle()
    LED2.turnOff()
    
