
/**
Library for MK2Robot control and some effectors we use in The Little Factory
see project repo @ https://github.com/Beauchef-Proyecta/mlf

This library has been written following the Arduino documentation and guidelines
https://www.arduino.cc/en/Hacking/LibraryTutorial
https://www.arduino.cc/en/Reference/APIStyleGuide
*/


#include <Arduino.h>
#include <Servo.h>

#include "MyLittleFactory.h"
#include "component_joints.h"

/**
 * @brief Prepare all components and wrapper functions
 *
 */

Joint joints[3];

int set_joint_position(int* params) {
    int id = params;
    joints[id].set_position(params++);
}

/**
 * @brief Build Command List
 *
 */

func_ptr_t command_list[256];

void build_command_list() {
    command_list[0] = set_joint_position;
    command_list[1] = set_joint_position;
    command_list[2] = set_joint_position;
}

/**
 * @brief Set the up gpio object
 *
 */
void setup_gpio() {
    joints[0] = Joint(SERVO_J0, HOME_J0);
    joints[1] = Joint(SERVO_J1, HOME_J1);
    joints[2] = Joint(SERVO_J2, HOME_J2);

    Serial.begin(115200);
}

/**
 * @brief Set joint position to home default
 *
 */
void send_robot_to_home() {}

/* move_axis */

/**
 * @brief Parse serial input
 *
 * @param bytes
 * @return int
 */

char* read_command() {
    char buffer[3];
    Serial.readBytes(buffer, 3);
    return buffer;
};

int execute_command(char* params) { return command_list[0]((int*)params); };

void write_response(int response) {};