
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
    int id = params[0] & 3;
    Serial.print(id);
    return joints[id].set_position(params[1]);
}

/**
 * @brief Build Command List
 *
 */

func_ptr_t command_list[256] = {};

void build_command_list() {
  // IMPORTANT: DO NOT assign 0x00; it is reserved for no-command!!
    command_list[SET_JOINT_POSITION] = set_joint_position;
}

/**
 * @brief Set the up gpio object
 *
 */

void setup_serial(){  
  Serial.begin(115200);
  Serial.setTimeout(20);
  Serial.flush();
  delay(100);
}
 
void setup_gpio() {
    joints[0] = Joint(SERVO_J0, HOME_J0);
    joints[1] = Joint(SERVO_J1, HOME_J1);
    joints[2] = Joint(SERVO_J2, HOME_J2);

    build_command_list();
}

/**
 * @brief Set joint position to home default
 *
 */
void send_robot_to_home() {}


/**
 * @brief Parse serial input
 *
 * @param bytes
 * @return int
 */

void read_command(char buffer[]) { // send data only when you receive data:
  memset(buffer, 0, 8);
  if (Serial.available() > 0){
    Serial.readBytesUntil(0xFE,buffer,8);
  }
  
};

/**
 * @brief execute command
 * 
 * @param cmd 
 * @return int 
 */

int execute_command(char cmd[]) { 
  int cmd_index = (cmd[0] & 0xF0);
  int response;
  if (command_list[cmd_index] != 0) {
    Serial.print("recieved command: 0x");
    Serial.print(cmd_index, HEX);
    Serial.print("-> status:");
    
    response = command_list[cmd_index](cmd);
    Serial.println(response, HEX);
  }
};
