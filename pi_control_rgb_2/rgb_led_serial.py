from time import sleep

class RGBLED:

    # delay (in seconds) to be used in colorCycle method
    color_cycle_delay = 0.01
    
    # initializes LED with unique ID. Must be a single character converted to bytes
    # example: b"1"
    # you also need to pass in a reference to a serial object
    def __init__(self, ID, ser):
        self.ID = ID
        self.ser = ser
    
    # sends serial message to arduino which it uses to 
    # change the color of the RGB LED
    def setColor(self, r, g, b):
        self.ser.write(self.ID)
        self.ser.write(r.to_bytes(length=1,byteorder='big'))
        self.ser.write(g.to_bytes(length=1,byteorder='big'))
        self.ser.write(b.to_bytes(length=1,byteorder='big'))

    # tells the arduino to make the LED cycle through color spectrum
    def colorCycle(self):
        # transition from red to yellow
        for x in range(256):
            self.setColor(255, x, 0)
            sleep(self.color_cycle_delay)
        
        # transition to green
        for x in range(255, 0, -1):
            self.setColor(x, 255, 0)
            sleep(self.color_cycle_delay)
            
        # transition to teal
        for x in range(256):
            self.setColor(0, 255, x)
            sleep(self.color_cycle_delay)
        
        # transition to blue
        for x in range(255, 0, -1):
            self.setColor(0, x, 255)
            sleep(self.color_cycle_delay)
        
        # transition to pink
        for x in range(256):
            self.setColor(x, 0, 255)
            sleep(self.color_cycle_delay)
        
        # transition back to red
        for x in range(255, 0, -1):
            self.setColor(255, 0, x)
            sleep(self.color_cycle_delay)
   
    def turnOff(self):
        self.setColor(0, 0, 0)
