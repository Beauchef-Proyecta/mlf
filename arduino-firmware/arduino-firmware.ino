#include "MyLittleFactory.h"


char cmd[8];

void setup() {
  //Attach servos
  //Homing inicial
  setup_serial();
  setup_gpio();

}
void loop() {
  read_command(cmd);
  execute_command(cmd);
}
