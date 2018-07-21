import network
import wifi_config
from umqtt_simple import MQTTClient
import mqtt_config
from sht30 import SHT30
from machine import Pin
from time import sleep

wifi = network.WLAN(network.STA_IF)

if not wifi.isconnected():
	wifi.active(True)
	wifi.connect(wifi_config.NAME, wifi_config.PASSWORD)
	while not wifi.isconnected():
		sleep(1)

c = MQTTClient(mqtt_config.CLIENT_ID, mqtt_config.SERVER)
c.set_last_will(b"sensors/status/" + mqtt_config.CLIENT_ID, "OFFLINE")
c.connect()
c.publish(b"sensors/status/" + mqtt_config.CLIENT_ID, b"ONLINE")

sensor = SHT30()
blue_led = Pin(2, Pin.OUT)

while True:
        blue_led.off()
        temperature, humidity = sensor.measure()
	c.publish(b"sensors/temperature/" + mqtt_config.CLIENT_ID, str(temperature))
	c.publish(b"sensors/humidity/" + mqtt_config.CLIENT_ID, str(humidity))
        blue_led.on()
	sleep(10 * 60)
