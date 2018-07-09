from time import sleep
from machine import I2C, Pin
import ssd1306

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

display.fill(0)
display.text("Wait...", 0, 0)
display.show()

sleep(1)

###################################################

import wifi_config
import network
wifi = network.WLAN(network.STA_IF)

if not wifi.isconnected():
	wifi.active(True)
	wifi.connect(wifi_config.NAME, wifi_config.PASSWORD)
	while not wifi.isconnected():
		sleep(1)

ip = wifi.ifconfig()[0].split('.')

display.fill(0)
display.text('IP:', 0, 0)
display.text(' ' + ip[0], 0, 10)
display.text('.' + ip[1], 0, 20)
display.text('.' + ip[2], 0, 30)
display.text('.' + ip[3], 0, 40)
display.show()

sleep(3)

###################################################

import mqtt_config
from umqtt_simple import MQTTClient

c = MQTTClient("umqtt_client", mqtt_config.SERVER)
c.connect()
c.publish(mqtt_config.TOPIC, b"HELLO")
c.disconnect()

###################################################

import dht
sensor = dht.DHT11(Pin(2))

while True:
	sensor.measure()

	c.connect()
	c.publish(mqtt_config.TOPIC, "TEMP:%d" % sensor.temperature())
	c.publish(mqtt_config.TOPIC, "HUMID:%d" % sensor.temperature())
	c.disconnect()

	display.fill(0)
	display.text("Temp:", 0, 0)
	display.text("%dc" % sensor.temperature(), 0, 12) # ºc - doesn't work
	display.text("Humid:", 0, 24)
	display.text("%d" % sensor.humidity(), 0, 36)
	display.show()

	sleep(30)



