#define LED1 12
#define LED2 13
#define ERRLED 11

void setup()
{

  // Set up LED outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);

  // Start serial communication at 115200 baud
  Serial.begin(9600);

  Serial.write('R');

}

int ledID;
int ledVal;

void loop() 
{

  if (Serial.available() > 1)
  {

    // Read 2 bytes
    ledID = Serial.read();
    ledVal = Serial.read();

    // Write LEDs accordingly
    if (ledID == '1')
    {
      analogWrite(LED1, ledVal);
    }
    else if (ledID == '2')
    {
      analogWrite(LED2, ledVal);
    }
    else
    {
      digitalWrite(ERRLED, HIGH);
    }
    
  }

}