import serial

ser = serial.Serial('COM3', 9600, timeout=1)
ser.reset_input_buffer()

arduino_ready_signal = 'R'

waiting = True

print("Waiting...")

# waits for the arduino to send a character indicating that it's ready to transmit data
while waiting:
    if ser.in_waiting > 0:
        char = ser.read(1).decode('utf-8')
        if char == arduino_ready_signal:
            print("Arduino is ready.")
            waiting = False
            
print("Done waiting.")

# sends message to arduino saying, "I'm ready to receive data!"
ser.write(b'R')

# initialize random float number
float = 1.2345

# convert float to string, then to bytes, then send over serial
ser.write(bytes(str(float), "utf-8"))

# send newline character so arduino knows when to stop reading
ser.write(b"\n")

# wait for arduino to send a response
while True:
    if ser.in_waiting > 0:

        # read a line, decode it, and remove newline character at the end
        float_returned = ser.readline().decode("utf-8").rstrip()

        # print value read to console
        print(float_returned)