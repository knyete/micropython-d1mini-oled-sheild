from time import sleep
from machine import I2C, Pin
import ssd1306
import oled_logo
import dht

sleep(1)

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

display.fill(0)
display.text("Wait...", 0, 0)
display.show()

sleep(1)

sensor = dht.DHT11(Pin(2))

while True:
	sensor.measure()
	display.fill(0)
	display.text("Temp:", 0, 0)
	display.text("%dc" % sensor.temperature(), 0, 12) # ºc - doesn't work
	display.text("Humid:", 0, 24)
	display.text("%d" % sensor.humidity(), 0, 36)
	display.show()
	sleep(30)



