# pi_arduino_serial
A collection of code for testing serial communication between raspberry pi and arduino

I use the pySerial library and the built-in arduino serial libary. URL for pySerial docs: https://pyserial.readthedocs.io/en/latest/pyserial_api.html 

## Projects:
pi_arduino_serial_test 1 and 2: copied code from a tutorial page to see if it works. Link to tutorial page: https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/#Arduino_code 

analog_serial: arduino sends analog value read from potentiometer to raspberry pi, gets it back, and lights up LED with that value

analog_serial_2 (in development): arduino sends 2 analog values to raspberry pi, gets them back, and lights up each LED with their respective value

mega_serial_test: tests the properties of the various built-in serial objects (Serial, Serial1, Serial2, Serial3)

pi_control_arduino: raspberry pi sends data to arduino, which it interprets and changes the brightnesses of 2 different LEDs

pi_control_rgb: raspberry pi sends data to arduino, which it interprets and changes the color of an RGB LED

pi_control_rgb_2: raspberry pi sends data to arduino, which it interprets and changes the colors of 2 different RGB LEDs