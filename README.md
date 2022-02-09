# Chemical pH tester
This repo includes electrical diagrams and micropython code to operate a chemical based pH tester with ESP8266 micro controller.

## Environmental Variable
A "env.py" file with the following items is needed for the operation of the provided micropython code.
* ssid = "your designated wifi name"
* password = "wifi password"
  * You may need to turn on compatibility mode for the ESP8266 controler as it only support older standards for wireless connections.
* WRITE_API_KEY = "your thingspeak api key"
