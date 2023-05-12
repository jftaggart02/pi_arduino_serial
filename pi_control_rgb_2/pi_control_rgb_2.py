import serial
import rgb_led_serial


# global variables
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


# here I create 2 RGBLED objects
LED1 = rgb_led_serial.RGBLED(b"1", ser)
LED2 = rgb_led_serial.RGBLED(b"2", ser)
        
    
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
    
