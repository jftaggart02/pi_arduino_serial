#include "rgb_led.h"

// Create RGB LED "LED1"
// Red pin: 10
// Green pin: 11
// Blue Pin: 12
// ID: '1'
RGBLED LED1(10, 11, 12);



void setup()
{

  // Begin serial communicaion at 9600 baud
  Serial.begin(9600);

  // Send message to computer saying, "I'm ready!"
  Serial.write('R');

}



byte data;
int i;



void loop() 
{

  // Read 3 bytes and set color of LED1 accordingly
  if (Serial.available() >= 3)
  {
    LED1.setColor(Serial.read(), Serial.read(), Serial.read());
  }

}
