// NOTE: This program only currently works with analog_serial.py

#define POT1 0
#define POT2 1
#define LED1 12
#define LED2 13
#define ERRLED 11


void setup()
{

  // Set up LED outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);

  // Start serial communication at 9600 baud
  Serial.begin(9600);

}

int pot1;
int pot2; 
int ledID;
int ledVal;
int i;

void loop() 
{

  // Read potentiometer values and map to value sendable in a single byte
  pot1 = map(analogRead(POT1), 0, 1023, 0, 255);
  pot2 = map(analogRead(POT2), 0, 1023, 0, 255);

  // Send pot1 ID and value read
  if (Serial.availableForWrite() > 1)
  {
    Serial.write(byte(1));
    Serial.write(byte(pot1));
  }
  
  // Send pot2 ID and value read
  if (Serial.availableForWrite() > 1)
  {
    Serial.write(byte(2));
    Serial.write(byte(pot2));
  }

  // Loop 2 times
  for (i = 0; i < 2; i++)
  {

    // Wait for reponse from pi
    while (1)
    {
      if (Serial.available() > 1)
      {
        break;
      }
    }

    // Read 2 bytes
    ledID = Serial.read();
    ledVal = Serial.read();

    // Write LEDs accordingly
    if (ledID == 1)
    {
      analogWrite(LED1, ledVal);
    }
    else if (ledID == 2)
    {
      analogWrite(LED2, ledVal);
    }
    else if (ledID == 0)
    {
      digitalWrite(ERRLED, HIGH);
    }

  }

}