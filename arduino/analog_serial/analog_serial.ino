#define POT1 0
#define LED 12



void setup()
{

  // Set LED pin to output
  pinMode(LED, OUTPUT);

  // Start serial communication at baud of 9600
  Serial.begin(9600);

}



int pot1;
int received;

void loop()
{

  // Read potentiometer voltage
  pot1 = analogRead(POT1);

  // Map to value between 0 and 255
  pot1 = map(pot1, 0, 1023, 0, 255);

  // Send potentiometer value to pi over serial
  Serial.write(byte(pot1));

  // Wait a bit for response
  delay(50);

  // Check to see if pi responded and write LED to value received
  if (Serial.available() > 0)
  {
    received = Serial.read();
    analogWrite(LED, received);
  }

}