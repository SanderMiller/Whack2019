#include <Adafruit_PN532.h>
#include <SPI.h>

int PN532_SCK = 2;
int PN532_MOSI = 3;
int PN532_SS = 4;
int PN532_MISO = 5;

Adafruit_PN532 nfc(PN532_SCK, PN532_MISO, PN532_MOSI, PN532_SS);

/*Adafruit_PN532 nfc(PN532_SS);*/

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
