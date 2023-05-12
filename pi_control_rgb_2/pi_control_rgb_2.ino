// PROGRAM FUNCTION: Reads serial messages from computer and makes 2 RGB LEDs light up accordingly

#include "rgb_led.h"

// Create RGB LED "LED1"
// Red pin: 12
// Green pin: 11
// Blue Pin: 10
// ID: '1'
RGBLED LED1(12, 11, 10, '1');

// Create RGB LED "LED2"
// Red pin: 9
// Green pin: 8
// Blue Pin: 7
// ID: '2'
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

  // If there are at least 4 bytes in input buffer
  if (Serial.available() >= 4)
  {
    // Read 4 bytes. 1st is LED ID and the other 3 are the values of red, green, and blue
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
