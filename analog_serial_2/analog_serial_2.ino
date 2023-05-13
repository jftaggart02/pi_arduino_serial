// PROGRAM FUNCTION: arduino sends 2 analog values to raspberry pi, gets them back, and lights up each LED with their respective value

#define POT1 0
#define POT2 1
#define LED1 11
#define LED2 12
#define ERRLED 13

void setup()
{

  // Set up LED outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);

  // Start serial communication at 9600 baud
  Serial.begin(9600);

  // Send message saying, "I'm ready!"
  Serial.write('R');

  // Wait for raspberry pi to say, "I'm ready!"
  bool waiting = true;
  char ch;
  while (waiting)
  {
    if (Serial.available() > 0)
    {
      ch = Serial.read();
      if (ch == 'R')
      {
        waiting = false;
      }
    }
  }

}

int pot1;
int pot2; 
int deviceType;
int deviceID;
int deviceVal;
int i;

void loop() 
{

  // Read potentiometer values and map to value sendable in a single byte
  pot1 = map(analogRead(POT1), 0, 1023, 0, 255);
  pot2 = map(analogRead(POT2), 0, 1023, 0, 255);

  // Send pot1 ID and value read
  if (Serial.availableForWrite() >= 3)
  {
    Serial.write('P');
    Serial.write('1');
    Serial.write(byte(pot1));
  }
  
  // Send pot2 ID and value read
  if (Serial.availableForWrite() >= 3)
  {
    Serial.write('P');
    Serial.write('2');
    Serial.write(byte(pot2));
  }

  // Loop 2 times
  for (i = 0; i < 2; i++)
  {

    // Wait for reponse from pi
    while (1)
    {
      if (Serial.available() >= 3)
      {
        break;
      }
    }

    // Read 3 bytes
    deviceType = Serial.read();
    deviceID = Serial.read();
    deviceVal = Serial.read();

    // Write LEDs accordingly
    if (deviceType == 'L')
    {
      if (deviceID == '1')
      {
        analogWrite(LED1, deviceVal);
      }
      else if (deviceID == '2')
      {
        analogWrite(LED2, deviceVal);
      }
      else
      {
        digitalWrite(ERRLED, HIGH);
      }

    }

  }

}