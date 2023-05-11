class RGBLED {
  public:
    int redPin;
    int greenPin;
    int bluePin;
    RGBLED(int r, int g, int b);
    void setColor(int red, int green, int blue);
};



// Create RGB LED "LED1"
// Red pin: 12
// Green pin: 11
// Blue Pin: 10
RGBLED LED1(12, 11, 10);



void setup() {}



int i;

void loop() 
{

  // Transition from red through orange and yellow
  for (i = 0; i <= 255; i++) {
    LED1.setColor(255, i, 0);
    delay(20);
  }

  // Transition to green
  for (i = 255; i >= 0; i--) {
    LED1.setColor(i, 255, 0);
    delay(10);
  }

  // Transition to teal
  for (i = 0; i <= 255; i++) {
    LED1.setColor(0, 255, i);
    delay(10);
  }

  // Transition to blue
  for (i = 255; i >= 0; i--) {
    LED1.setColor(0, i, 255);
    delay(10);
  }

  // Transition to pink
  for (i = 0; i <= 255; i++) {
    LED1.setColor(i, 0, 255);
    delay(10);
  }
  
  // And back to red
  for (i = 255; i >= 0; i--) {
    LED1.setColor(255, 0, i);
    delay(10);
  }

}



void RGBLED::setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

RGBLED::RGBLED(int r, int g, int b) {
  redPin = r;
  greenPin = g;
  bluePin = b;
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}
