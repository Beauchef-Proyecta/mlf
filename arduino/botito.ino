#include <Servo.h>
#define pin_base 3
#define pin_L1 5
#define pin_L2 6
#define pin_eff 9 //manage gripper
#define pin_grip 7 //manage relay
#define pin_belt 8 //manage belt status
#define pin_belt_turn 4 //manage belt forward-backward

Servo base;
Servo L1;
Servo L2;
Servo eff;

int poser = 0; // initial position of server
int val; // initial value of input
#define INPUT_SIZE 30


//Homing
void axis_home() {
  base.write(90);
  L1.write(90);
  L2.write(90);
  eff.write(90);

}

void setup() {
  //Attach servos
  Serial.begin(115200);
  base.attach(pin_base);
  L1.attach(pin_L1);
  L2.attach(pin_L2);
  eff.attach(pin_eff);
  pinMode(pin_grip, OUTPUT);
  pinMode(pin_belt, OUTPUT);
  digitalWrite(pin_grip, LOW); //relay init off
  digitalWrite(pin_belt, LOW); //belt init off

  //Homing inicial
  axis_home();

}
void loop() {

  // Get next command from Serial (add 1 for final 0)
  char input[INPUT_SIZE + 1];
  byte size = Serial.readBytes(input, INPUT_SIZE);
  // Add the final 0 to end the C string
  input[size] = 0;

  // Read each command pair
  char* command = strtok(input, "&");

  while (command != 0)
  {
    // Split the command in two values
    char* separator = strchr(command, ':');

    if (separator != 0)
    {
      // Actually split the string in 2: replace ':' with 0
      *separator = 0;
      int servoId = atoi(command);
      //Serial.println(servoId);
      ++separator;
      int position = atoi(separator);
      //Serial.println(position);

      // Do something with servoId and position
      move_axis(servoId, position);
    }

    // Find the next command in input string
    command = strtok(0, "&");
  }
}

//move_axis function
void move_axis(int servoId, int position) {
  if (servoId == 1) {
    base.write(position);

  }

  if (servoId == 2) {
    L1.write(position);

  }

  if (servoId == 3) {
    L2.write(position);

  }

  if (servoId == 4) {
    eff.write(position);

  }
  if (servoId == 5) {
    if (position == 1) {
      digitalWrite(pin_grip, HIGH);
    }
    if (position == 0) {
      digitalWrite(pin_grip, LOW);
    }
  }
  if (servoId == 6) {
    if (position == 1) {
      digitalWrite(pin_belt, HIGH);
    }
    if (position == 0) {
      digitalWrite(pin_belt, LOW);
    }
  }
  if (servoId == 7) {
    if (position == 1) {
      digitalWrite(pin_belt_turn, HIGH); //forward
    }
    if (position == 0) {
      digitalWrite(pin_belt_turn, LOW); //backward
    }
  }

}
