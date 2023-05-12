#ifndef RGB_LED_H
#define RGB_LED_H

class RGBLED {
  public:
    int redPin;
    int greenPin;
    int bluePin;
    RGBLED(int r, int g, int b);
    void setColor(int red, int green, int blue);
};

#endif