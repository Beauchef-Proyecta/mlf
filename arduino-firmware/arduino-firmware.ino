
#include "MyLittleFactory.h"



void setup() {
  //Attach servos
  Serial.begin(115200);
  //Homing inicial
  axis_home();

}
void loop() {
  do_everything();
}