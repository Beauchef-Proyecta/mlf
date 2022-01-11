#include "component_joints.h"

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
