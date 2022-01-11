#include "MyLittleFactory.h"

int response;
char* cmd;

void setup() {
  //Attach servos
  //Homing inicial
  setup_gpio();

}
void loop() {
  cmd = read_command();
  Serial.print(cmd);
  response = execute_command(cmd);
  write_response(response);
}
