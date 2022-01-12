#include "MyLittleFactory.h"

void setup() {
    setup_serial();
    setup_components();
    build_command_list();
}
void loop() {
    char cmd[8];
    read_command(cmd);
    execute_command(cmd);
}
