# Chemical pH Tester
This repo includes electrical diagrams and micropython code to operate a chemical based pH tester with ESP8266 micro controller.

## Environmental Variable
A "env.py" file with the following items is needed for the operation of the provided micropython code.
* ssid = "your designated wifi name"
* password = "wifi password"
  * You may need to turn on compatibility mode for the ESP8266 controler as it only support older standards for wireless connections.
* WRITE_API_KEY = "your thingspeak api key"

## Parts List
* 3V relay electrical switch (2)
* 3V submersible pump (2)
* White LED (2)
* Plastic colored filters (Red & Blue)
* Light sensor TSL2591
* Rubber tubes
* 3D printed housing
* 3D printed reservoir for dye
* Buoyant platform
* Microcontroller (ESP8266)
* External RTC (DS3231)

## Project Report
[Complete Project Report in PDF](ProjectReport.pdf)