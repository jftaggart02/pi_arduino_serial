#include <RC_Receiver.h>

RC_Receiver receiver(13,11,9,7,5);
/* Ch1: 13
 * Ch2: 11
 * Ch3: 9
 * Ch4: 7
 * Ch5: 5
 */

//Channel min and max value
//Leave the default value for the un used channels
//Invert the min and max val to reverse
int minMax[5][2] = { 
// Min   Max
	{1088,1880},  // Ch1: Throttle
	{1088,1873},  // Ch2: Elevator
	{1085,1871},  // Ch3: Aileron (Max to the left and min to the right)
	{1090,1875},  // Ch4: Rudder (Max to the left and min to the right)
    {1080,1880}  // Ch5: Gear Channel (kill switch) (0 = 1880) (1 = 1080)
                // Ch6: Aux channel (0 = 1880) (1/2 = 1480) (1 = 1080)
};

// Includes required to use Roboclaw library
#include <SoftwareSerial.h>
#include "RoboClaw.h"

// See limitations of Arduino SoftwareSerial
// Rx pin: 0
// TX pin: 1
SoftwareSerial serial(0,1);	
RoboClaw roboclaw(&serial,10000);

// Addresses (in hexadecimal) of each of the 4 motor controllers
#define left_front 0x81
#define right_front 0x82
#define left_rear 0x83
#define right_rear 0x84

/******************************************************************************
NOIE: To run a motor forward at a certain speed, use the following command:

roboclaw.ForwardM1(address of motor, speed from 0 to 128);

To run it backwards, use this command:

roboclaw.BackwardM1(address of motor, speed from 0 to 128);

To run it forwards or backwards, use this command:

roboclaw.ForwardBackwardM1(address of motor, speed from 0 to 128);
 > 0 to 63 runs it backwards
 > 64 stops motor
 > 65 to 128 runs it forwards

Once the speed has been set, the motor will continue at that speed until it
receives another command.
******************************************************************************/

// Motor slew rate delay in ms
int motor_slew_delay = 20;

void setup() {
    
    // Begin serial communication with motor controllers
    roboclaw.begin(115200);

    // Set min and max values for receiver channels
    receiver.setMinMax(minMax);

    // Begin serial communication with computer
    Serial.begin(9600);

    // Send message to computer saying, "I'm ready!"
    Serial.write('R');

}

byte id, desired_speed;
byte desired_speed_left, desired_speed_right;
byte actual_speed_left = 64;
byte actual_speed_right = 64;

void loop() {

    // Get RC switch value

    // If switch is on
        // RC logic

    // Else

    // If there are 4 bytes in the input buffer
    if (Serial.available() >= 4) {

        id = Serial.read();
        desired_speed = Serial.read();

        if (id == 'r') {

            desired_speed_right = desired_speed;

        }

        else if (id == 'l') {

            desired_speed_left = desired_speed;

        }

        id = Serial.read();
        desired_speed = Serial.read();

        if (id == 'r') {

            desired_speed_right = desired_speed;

        }

        else if (id == 'l') {

            desired_speed_left = desired_speed;

        }

    }

    // If we stopped receiving data from computer
    else {

        // Set desired speed to stopped
        desired_speed_left = 64;
        desired_speed_right = 64;

    }

    if (actual_speed_left < desired_speed_left) {

        actual_speed_left++;

    }

    else if (actual_speed_left > desired_speed_left) {

        actual_speed_left--;

    }

    if (actual_speed_right < desired_speed_right) {

        actual_speed_right++;

    }

    else if (actual_speed_right > desired_speed_right) {

        actual_speed_right--;

    }

    // Set left motor speeds
    roboclaw.ForwardBackwardM1(left_front,  actual_speed_left);
    roboclaw.ForwardBackwardM1(left_rear,   actual_speed_left);

    // Set right motor speeds
    roboclaw.ForwardBackwardM1(right_front, actual_speed_right);
    roboclaw.ForwardBackwardM1(right_rear,  actual_speed_right);
    
    // Motor slew delay
    delay(motor_slew_delay);
    
}