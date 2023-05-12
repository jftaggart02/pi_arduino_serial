#include "rgb_led.h"

// Sets LED to a certain color
void RGBLED::setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

// Constructor
RGBLED::RGBLED(int r, int g, int b, char id) {
  redPin = r;
  greenPin = g;
  bluePin = b;
  ID = id;
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}
