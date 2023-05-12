// What I found out by running this program:
// - Serial sends and receives data through USB cable while Serial1, Serial2, and Serial3 don't

// This shouldn't output anything to the serial monitor.
// /*
void setup()
{
  Serial1.begin(9600);
}

void loop()
{
  Serial1.println("Testing");
  delay(2000);
}
// */

// This should output stuff to the serial monitor.
/*
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.println("Testing");
  delay(2000);
}
*/