
/**
Library for MK2Robot control and some effectors we use in The Little Factory
see project repo @ https://github.com/Beauchef-Proyecta/mlf

This library has been written following the Arduino documentation and guidelines
https://www.arduino.cc/en/Hacking/LibraryTutorial
https://www.arduino.cc/en/Reference/APIStyleGuide
*/


/**GPIO DEFINITIONS */
#define SERVO_J0 3
#define SERVO_J1 5
#define SERVO_J2 6
#define GRIPPER_SERVO 9   // gripper
#define GRIPPER_RELAY 7   // manage relay
#define BELT_STATUS 8     // manage belt status
#define BELT_DIRECTION 4  // manage belt forward-backward

/* HOME VALUES */
#define HOME_J0 90
#define HOME_J1 90
#define HOME_J2 90
#define HOME_GRIPPER 90


typedef int (*func_ptr_t)(char*);

void build_command_list();

void setup_gpio();

void send_robot_to_home();

void read_command(char* buffer);

int execute_command(char* cmd);

void write_response(int response);
