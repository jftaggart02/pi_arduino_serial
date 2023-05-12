# import pySerial library
import serial
# import file rgb_led_serial.py
import rgb_led_serial


# Here, I create a serial object with the pySerial library
# arguments: 
#   > address of serial port
#   > baud rate
ser = serial.Serial('COM6', 9600)

# What address do I put in as the first argument?
#   > on raspberry pi: 
#     > run ls dev/tty* and see if there's an "ACMX" or "USBX"
#       > the "X" is a placeholder for some digit
#     > put in either "/dev/ttyACMX" or "/dev/ttyUSBX"
#   > on windows machine:
#     > go to arduino IDE and find out what port the arduino is connected to
#     > it might be "COM6" for example

    
# waits for the arduino to send a character indicating that it's ready to receive data
def wait_for_arduino():

    # waits to receive this character
    arduino_ready_signal = 'R'
    
    waiting = True
    
    print("Waiting...")

    while waiting:
        if ser.in_waiting > 0:
            char = ser.read(1).decode('utf-8')
            if char == arduino_ready_signal:
                print("Arduino is ready.")
                waiting = False
                
    print("Done waiting.")


# here I create 2 RGBLED objects
# arguments: 
#   > unique ID for each LED (must be converted to bytes)
#   > serial object created earlier
LED1 = rgb_led_serial.RGBLED(b"1", ser)
LED2 = rgb_led_serial.RGBLED(b"2", ser)
        
    
# in case there was anything in the input buffer I didn't want, I clear it
ser.reset_input_buffer()


# wait for arduino to be ready
wait_for_arduino()


# now you can do whatever you want here with the LED objects created!
while True:
    LED1.colorCycle()
    LED1.turnOff()
    LED2.colorCycle()
    LED2.turnOff()
    
