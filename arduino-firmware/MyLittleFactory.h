
/**
Library for MK2Robot control and some effectors we use in The Little Factory
see project repo @ https://github.com/Beauchef-Proyecta/mlf

This library has been written following the Arduino documentation and guidelines
https://www.arduino.cc/en/Hacking/LibraryTutorial
https://www.arduino.cc/en/Reference/APIStyleGuide
*/

#include <Servo.h>

/* GPIO DEFINITIONS */
#define SERVO_J0 3
#define SERVO_J1 5
#define SERVO_J2 6
#define GRIPPER_SERVO 9   // gripper
#define GRIPPER_RELAY 7   // manage relay
#define BELT_STATUS 8     // manage belt status
#define BELT_DIRECTION 4  // manage belt forward-backward

/* PROGRAM PARAMETERS */
#define INPUT_SIZE 30

/* HOME VALUES */
#define HOME_J0 90
#define HOME_J1 90
#define HOME_J2 90
#define HOME_GRIPPER 90

class Joint {
   private:
    Servo servo;
    int position;

   public:
    Joint();
    Joint(int pin, int position);

    int set_position(int* params);
};

typedef int (*func_ptr_t)(int*);

void set_gpio();

void axis_home();

int move_axis(int servoId, int position);

void do_everything();