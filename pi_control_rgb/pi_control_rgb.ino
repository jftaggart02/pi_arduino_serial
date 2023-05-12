// PROGRAM FUNCTION: Reads serial messages from computer and makes an RGB LED light up accordingly

#include "rgb_led.h"

// Create RGB LED "LED1"
// Red pin: 12
// Green pin: 11
// Blue Pin: 10
RGBLED LED1(12, 11, 10);

void setup()
{

  // Begin serial communicaion at 9600 baud
  Serial.begin(9600);

  // Send message to computer saying, "I'm ready!"
  Serial.write('R');

}

byte r, g, b;
int i;

void loop() 
{

  // Read 3 bytes and set color of LED1 accordingly
  if (Serial.available() >= 3)
  {
    r = Serial.read();
    g = Serial.read();
    b = Serial.read();
    LED1.setColor(r, g, b);
  }

}
