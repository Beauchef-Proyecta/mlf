#include "MyLittleFactory.h"

int response;
char cmd[8];

void setup() {
  //Attach servos
  //Homing inicial
  setup_gpio();

}
void loop() {
  memset(cmd, '.', 8);
  read_command(cmd);
  response = execute_command(cmd);
}
