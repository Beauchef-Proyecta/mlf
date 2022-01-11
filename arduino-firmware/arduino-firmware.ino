
#include "MyLittleFactory.h"



void setup() {
  //Attach servos
  Serial.begin(115200);
  //Homing inicial
  set_gpio();
  axis_home();

}
void loop() {
  do_everything();
}
