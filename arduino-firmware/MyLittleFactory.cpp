
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

int set_joint_position(char params[]) {
  
    Serial.println(params[0]);
    Serial.println(params[1]);
    int id = params[0];
    return joints[id].set_position(params[1]);
}

/**
 * @brief Build Command List
 *
 */

func_ptr_t command_list[256];

void build_command_list() {
    command_list[0x61] = set_joint_position;
    command_list[0x62] = set_joint_position;
    command_list[0x63] = set_joint_position;
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
    Serial.setTimeout(20);
    build_command_list();
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
int incomingByte = 0; // for incoming serial data
void read_command(char* buffer) { // send data only when you receive data:
  if (Serial.available() > 0){
    Serial.readBytesUntil(',',buffer,8);
  }
  
};

int execute_command(char cmd[]) { 
  int cmd_index = cmd[0];
  if (cmd_index != '.') {
    if (command_list[cmd_index] != 0) 
      Serial.println(command_list[cmd_index](cmd), DEC);
  }
};

void write_response(int response) {};
