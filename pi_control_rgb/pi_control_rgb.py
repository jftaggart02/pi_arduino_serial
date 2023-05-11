# import serial library
import serial
from time import sleep


# global variables
delay = 0.01
arduino_ready_signal = 'R'


# begin serial communication at baud of 9600
# run ls dev/tty* and see if there's an "ACMX" or "USBX"
# and change the serial address below accordingly.
ser = serial.Serial('COM6', 9600)


# sends serial message to arduino which it uses to 
# change the color of the RGB LED
def setColor(r, g, b):
    ser.write(r.to_bytes())
    ser.write(g.to_bytes())
    ser.write(b.to_bytes())
    
    
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
    

# tells the arduino to make the LED cycle through color spectrum
def color_cycle():
    # transition from red to yellow
    for x in range(256):
        setColor(255, x, 0)
        sleep(delay)
    
    # transition to green
    for x in range(255, 0, -1):
        setColor(x, 255, 0)
        sleep(delay)
        
    # transition to teal
    for x in range(256):
        setColor(0, 255, x)
        sleep(delay)
    
    # transition to blue
    for x in range(255, 0, -1):
        setColor(0, x, 255)
        sleep(delay)
    
    # transition to pink
    for x in range(256):
        setColor(x, 0, 255)
        sleep(delay)
    
    # transition back to red
    for x in range(255, 0, -1):
        setColor(255, 0, x)
        sleep(delay)
        
    
# in case there was anything in the input buffer we didn't want,
# we clear it
ser.reset_input_buffer()


# wait for arduino to be ready
wait_for_arduino()


while True:
    color_cycle()
    