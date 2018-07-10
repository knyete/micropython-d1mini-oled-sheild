from time import sleep
from machine import Pin

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

blue_led = Pin(2, Pin.OUT)

for i in range(3):
	blue_led.on()
	sleep(0.5)
	blue_led.off()
	sleep(0.5)

###################################################

import mqtt_config
from umqtt_simple import MQTTClient

c = MQTTClient(mqtt_config.CLIENT_ID, mqtt_config.SERVER)
c.connect()
c.publish(mqtt_config.TOPIC, b"THERMOSTAT ONLINE")
c.disconnect()

###################################################

relay = Pin(4, Pin.OUT)

def rx(topic, msg):
	try:
		temp = int(msg)
	except ValueError:
		pass
	else:
		if temp > 22:
			relay.off()
			c.publish(mqtt_config.TOPIC, b"THERMOSTAT OFF")
		elif temp < 18:
			relay.on()
			c.publish(mqtt_config.TOPIC, b"THERMOSTAT ON")

c.set_callback(rx)
c.connect()
c.subscribe(mqtt_config.TOPIC)

try:
    while 1:
        c.wait_msg()
finally:
	c.disconnect()


