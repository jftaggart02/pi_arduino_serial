#include "rgb_led.h"

// Create RGB LED "LED1"
// Red pin: 12
// Green pin: 11
// Blue Pin: 10
RGBLED LED1(12, 11, 10, '1');

// Create RGB LED "LED2"
// Red pin: 9
// Green pin: 8
// Blue Pin: 7
RGBLED LED2(9, 8, 7, '2');



void setup()
{

  // Begin serial communicaion at 9600 baud
  Serial.begin(9600);

  // Send message to computer saying, "I'm ready!"
  Serial.write('R');

}



byte r, g, b, id;
int i;



void loop() 
{

  // Read 3 bytes and set color of LED1 accordingly
  if (Serial.available() >= 4)
  {
    id = Serial.read();
    r = Serial.read();
    g = Serial.read();
    b = Serial.read();
    if (id == '1')
    {
      LED1.setColor(r, g, b);
    }
    else if (id == '2')
    {
      LED2.setColor(r, g, b);
    }
    
  }

}
