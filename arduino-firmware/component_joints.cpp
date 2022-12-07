#include "component_joints.h"
#include "Arduino.h"

Joint::Joint(){};

Joint::Joint(int pin, uint8_t position) {
    this->servo.attach(pin);
    int params[] = {pin, position};
    this->set_position(position);
};

uint8_t Joint::set_position(uint8_t position) {
    this->position = position;
    this->servo.write(position);
    return this->position;
};



Magnet::Magnet(){};

Magnet::Magnet(int pin, int status) {
    this->pin = pin;
    this->set_status(status);
};

uint8_t Magnet::set_status(uint8_t status) {
    this->status = (int)status;
    digitalWrite(this->pin,(int) status);
    return this->status;
};
