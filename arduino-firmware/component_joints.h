#include <Servo.h>

class Joint {
   private:
    Servo servo;
    int position;

   public:
    Joint();
    Joint(int pin, int position);

    int set_position(int* params);
};
