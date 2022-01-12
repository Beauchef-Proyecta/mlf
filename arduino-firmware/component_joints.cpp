#include "component_joints.h"

Joint::Joint(){};

Joint::Joint(int pin, int position) {
    this->servo.attach(pin);
    int params[] = {pin, position};
    this->set_position(position);
};

int Joint::set_position(int position) {
    this->position = position;
    this->servo.write(position);
    return this->position;
};
