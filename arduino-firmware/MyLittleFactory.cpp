
/**
Library for MK2Robot control and some effectors we use in The Little Factory
see project repo @ https://github.com/Beauchef-Proyecta/mlf

This library has been written following the Arduino documentation and guidelines
https://www.arduino.cc/en/Hacking/LibraryTutorial
https://www.arduino.cc/en/Reference/APIStyleGuide
*/

#include "MyLittleFactory.h"

#include <Servo.h>

Joint::Joint(){};

Joint::Joint(int pin, int position) {
    this->servo.attach(pin);
    int params[] = {pin, position};
    this->set_position(params);
};

int Joint::set_position(int *params) {
    int val = params;
    this->position = val;
    this->servo.write(val);
};

Joint joints[3];

int set_joint_position(int *params) {
    int id = params;
    joints[id].set_position(params++);
}

/* Command List */

func_ptr_t command_list[256];

void build_command_list() {
    command_list[0] = set_joint_position;
    command_list[1] = set_joint_position;
    command_list[2] = set_joint_position;
}



/******************
  Peripheral Setup
*******************/
void set_gpio() {
    joints[0] = Joint(SERVO_J0, 0);
    joints[1] = Joint(SERVO_J1, 0);
    joints[2] = Joint(SERVO_J2, 0);
}

/* Homing */
void axis_home() {}

/* move_axis */
void move_axis(int servoId, int position){
  int params[] = {servoId, position};
  command_list[0](params);
    /*
    if (servoId == 1) {
      base.write(position);

    }

    if (servoId == 2) {
      L1.write(position);

    }

    if (servoId == 3) {
      L2.write(position);

    }

    if (servoId == 4) {
      eff.write(position);

    }
    if (servoId == 5) {
      if (position == 1) {
        digitalWrite(pin_grip, HIGH);
      }
      if (position == 0) {
        digitalWrite(pin_grip, LOW);
      }
    }
    if (servoId == 6) {
      if (position == 1) {
        digitalWrite(pin_belt, HIGH);
      }
      if (position == 0) {
        digitalWrite(pin_belt, LOW);
      }
    }
    if (servoId == 7) {
      if (position == 1) {
        digitalWrite(pin_belt_turn, HIGH); //forward
      }
      if (position == 0) {
        digitalWrite(pin_belt_turn, LOW); //backward
      }
    }
    */

};

/* main */
void do_everything(){

};