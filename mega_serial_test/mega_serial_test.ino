
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