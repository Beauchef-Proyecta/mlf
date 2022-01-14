#include <Servo.h>

class Joint {
   private:
    Servo servo;
    uint8_t position;

   public:
    Joint();
    Joint(int pin, uint8_t position);

    uint8_t set_position(uint8_t position);
};
