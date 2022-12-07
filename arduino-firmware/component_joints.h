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

class Magnet {
   private:
    int pin;
    int status;

   public:
    Magnet();
    Magnet(int pin, int status);

    uint8_t set_status(uint8_t position);
};
