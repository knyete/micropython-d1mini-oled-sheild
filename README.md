# MicroPython

## Wemos D1 Mini

### OLED Shield

![IMG_20160617_112945.jpg](./IMG_20160617_112945.jpg)

https://forum.micropython.org/viewtopic.php?t=1637#p11474

https://wiki.wemos.cc/products:retired:oled_shield_v1.1.0

https://github.com/wendlers/mpfshell

https://github.com/adafruit/micropython-adafruit-ssd1306/blob/master/ssd1306.py

https://docs.micropython.org/en/latest/esp8266/library/machine.I2C.html

`mpfshell -s main.mpf`

(Then restart the MCU.)

https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/shields.html#oled

### DHT Shield

https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/shields.html#dht-and-dht-pro

### Wifi

https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_basics.html

https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html#network

### MQTT

https://github.com/micropython/micropython-lib/tree/master/umqtt.simple

https://mosquitto.org/

`sudo apt-get install mosquitto mosquitto-clients`

`mosquitto_sub -t sensors/temperature -q 1`

iPhone app: MQTTTester

### Thermostat

https://en.wikipedia.org/wiki/PID_controller

https://github.com/B3AU/micropython/blob/master/PID.py

https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_sub_led.py









