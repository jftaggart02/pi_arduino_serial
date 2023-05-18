void setup()
{
	
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

String float_str;
float float_received;

void loop()
{

  // Wait for computer to send data
  if (Serial.available() > 0)
  {
    // Read one line
    float_str = Serial.readStringUntil('\n');

    // Convert to a float
    float_received = float_str.toFloat();

    // Send it back
    Serial.println(float_received, 6);
    
  }

}


