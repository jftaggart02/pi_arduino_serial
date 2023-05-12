#include "rgb_led.h"

// Sets color of LED to a specified RGB value
void RGBLED::setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

// Constructor
RGBLED::RGBLED(int r, int g, int b) {
  redPin = r;
  greenPin = g;
  bluePin = b;
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}
