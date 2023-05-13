# pi_arduino_serial
A collection of code for testing serial communication between raspberry pi and arduino

I use the pySerial library and the built-in arduino serial libary. URL for pySerial docs: https://pyserial.readthedocs.io/en/latest/pyserial_api.html 

## Tutorial (in progress):
### Creating a serial object:
    ser = serial.Serial(port, baudrate)

For the "port" parameter, put the address of the serial port you want to send data to and receive data from. If you're using your personal computer, you can find in the Arduino IDE the name of the port your arduino's connected to. It might be something like "COM6". You'd put it in quotes like this:

    ser = serial.Serial("COM6", 9600)

If you're using a raspberry pi, run this command in the linux terminal:

    ls /dev/tty*

It'll pull up a huge list of everything that starts with "/dev/tty". You might see "/dev/ttyACMX" or "/dev/ttyUSBX". The "X" is a placeholder for any digit. That's the address of the port your arduino's connected to. You'd put it in the parameter like this:

    ser = serial.Serial("/dev/ttyACM0", 9600)

The "baudrate" parameter is, simply put, how fast data can be transferred. A very common baud rate you see is 9600, but you can go up to 115200 on the arduino.

There are other parameters like timeout and write_timeout, but I didn't need them for most of my projects. You can see the pySerial docs for more info about those.

### Reading bytes:
    data = ser.read(1)

This example reads 1 byte from the input buffer and stores it in "data". The parameter is how many bytes you want to read from the input buffer.

If you're expecting to read a character or string using this method, you'll need to decode it because "read()" returns an instance of "bytes". For example:

    if ser.read(1).decode("utf-8") == "A":
        # do something

If you're expecting to receive a number, you'll want to convert it to an integer before using it later on in your program. For example:

    data_as_byte = ser.read(1)
    data_as_int = int.from_bytes(data_as_byte, "big")
    if data_as_int == 5:
        # do something

Usually the "read()" method is used together with the "in_waiting" attribute, which returns the number of bytes available to read in the input buffer. For example:

    if ser.in_waiting > 0:
        data = ser.read(1).decode("utf-8")
        if data == "A":
            # do something

## Projects:
- **pi_arduino_serial_test 1 and 2:** copied code from a tutorial page to see if it works. Link to tutorial page: https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/#Arduino_code 

- **analog_serial:** arduino sends analog value read from potentiometer to raspberry pi, gets it back, and lights up LED with that value

- **analog_serial_2:** arduino sends 2 analog values to raspberry pi, gets them back, and lights up each LED with their respective value

- **mega_serial_test:** tests the properties of the various built-in serial objects (Serial, Serial1, Serial2, Serial3)

- **pi_control_arduino:** raspberry pi sends data to arduino, which it interprets and changes the brightnesses of 2 different LEDs

- **pi_control_rgb:** raspberry pi sends data to arduino, which it interprets and changes the color of an RGB LED

- **pi_control_rgb_2:** raspberry pi sends data to arduino, which it interprets and changes the colors of 2 different RGB LEDs