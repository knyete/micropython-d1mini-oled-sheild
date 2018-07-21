from machine import I2C, Pin
from time import sleep
import network
import wifi_config
import ssd1306
from umqtt_simple import MQTTClient
import mqtt_config

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(64, 48, i2c)
text_buffer = []

def display_print(text):
        global text_buffer
        text_buffer.append(text[0:8])
        if len(text_buffer) > 5:
                text_buffer.pop(0)
        display.fill(0)
        row = 0
        for line in text_buffer:
                display.text(line, 0, row)
                row += 10
        display.show()

display_print('START')

wifi = network.WLAN(network.STA_IF)

if not wifi.isconnected():
	wifi.active(True)
	wifi.connect(wifi_config.NAME, wifi_config.PASSWORD)
	while not wifi.isconnected():
		sleep(10)

def rx(topic, msg):
        print((topic, msg))
        display_print(msg)

mqtt = MQTTClient(mqtt_config.CLIENT_ID, mqtt_config.SERVER)
mqtt.set_last_will(b"display/status/" + mqtt_config.CLIENT_ID, "OFFLINE")
mqtt.set_callback(rx)
mqtt.connect()
mqtt.subscribe(b"#")
mqtt.publish(b"display/status/" + mqtt_config.CLIENT_ID, b"ONLINE")

blue_led = Pin(2, Pin.OUT)
blue_led_state = 0
blue_led.value(blue_led_state)

try:
    while 1:
        mqtt.wait_msg()
        blue_led_state += 1
        blue_led_state %= 2
        blue_led.value(blue_led_state)
        
finally:
	mqtt.disconnect()
