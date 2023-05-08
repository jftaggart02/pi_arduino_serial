#define BUTTON 13
#define POT1 0



void setup()
{

  // Set up button input
  pinMode(BUTTON, INPUT_PULLUP);

  // Start serial communication at baud of 9600
  Serial.begin(9600);

}



int pot1;

void loop()
{

  // Wait for button to be pressed
  while (1)
  {
    if (digitalRead(BUTTON) == HIGH)
    {
      break;
    }
  }

  // Read potentiometer voltage
  pot1 = analogRead(POT1);

  // Map to value between 0 and 255
  pot1 = map(pot1, 0, 1023, 0, 255);

  // Send potentiometer value to pi over serial
  Serial.write(byte(pot1));

}