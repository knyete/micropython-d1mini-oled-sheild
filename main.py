from time import sleep
from machine import I2C, Pin
import ssd1306
import oled_logo

sleep(2)

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

display.fill(0)
display.text("Micro", 0, 0)
display.text("Python", 0, 8)
display.show()

