## https://forum.micropython.org/viewtopic.php?t=1637

from machine import Pin, I2C
import ssd1306

logo = (
    0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000001, 0b10000000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000000, 0b00010000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000001, 0b10001000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000010, 0b01100000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000100, 0b01010000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000100, 0b00001000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000101, 0b00001000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00001101, 0b01001000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00011110, 0b01001000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00011111, 0b10011100, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00111111, 0b11111100, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00111111, 0b11111100, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00111111, 0b11111100, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00111011, 0b11111100, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00011011, 0b01111000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00011111, 0b01111000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00001111, 0b11111000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000111, 0b11110000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000111, 0b11110000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000110, 0b01100111, 0b00000000, 0b00000000,
    0b00000000, 0b00000001, 0b11001010, 0b01101111, 0b11100000, 0b00000000,
    0b00000000, 0b00000111, 0b11111010, 0b11111111, 0b01110000, 0b00000000,
    0b00000000, 0b00001101, 0b11110110, 0b11111100, 0b11110000, 0b00000000,
    0b00000000, 0b00011110, 0b01100100, 0b11110011, 0b11110000, 0b00000000,
    0b00000000, 0b00011111, 0b10010001, 0b11001111, 0b11101000, 0b00000000,
    0b00000000, 0b00010111, 0b11101101, 0b11111111, 0b11001000, 0b00000000,
    0b00000000, 0b00011011, 0b11000001, 0b11111110, 0b00111000, 0b00000000,
    0b00000000, 0b00111010, 0b11100001, 0b11010010, 0b01111100, 0b00000000,
    0b00000000, 0b00111100, 0b01011101, 0b11100011, 0b11111110, 0b00000000,
    0b00000000, 0b00111110, 0b01000001, 0b11111111, 0b11111110, 0b00000000,
    0b00000000, 0b00111111, 0b11100001, 0b11111111, 0b11111010, 0b00000000,
    0b00000000, 0b11111111, 0b11110010, 0b11111111, 0b11110011, 0b00000000,
    0b00000001, 0b11111011, 0b11111100, 0b01100100, 0b10010111, 0b10000000,
    0b00000001, 0b01111101, 0b01010001, 0b11001001, 0b00111110, 0b10000000,
    0b00000000, 0b10011111, 0b10001110, 0b10001011, 0b11111001, 0b00000000,
    0b00000001, 0b10100111, 0b11111111, 0b11111111, 0b11100101, 0b10000000,
    0b00000001, 0b01101001, 0b11111111, 0b11111111, 0b10010110, 0b10000000,
    0b00000010, 0b01011010, 0b01111111, 0b11111110, 0b01011010, 0b01000000,
    0b00000000, 0b10010110, 0b10011111, 0b11111001, 0b01101001, 0b00000000,
    0b00000000, 0b00100101, 0b10100111, 0b11100101, 0b10100100, 0b00000000,
    0b00000000, 0b00001001, 0b01101001, 0b10010110, 0b10010000, 0b00000000,
    0b00000000, 0b00000010, 0b01011010, 0b01011010, 0b01000000, 0b00000000,
    0b00000000, 0b00000000, 0b10010111, 0b11101001, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00100101, 0b10100100, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00001000, 0b00010000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,
)

i2c = I2C(-1, Pin(5), Pin(4))

display = ssd1306.SSD1306_I2C(64, 48, i2c)
display.fill(True)

for x in range(48):
    for y in range(48):
        display.pixel(8 + x, y, not logo[y * 6 + x // 8] & (1<<(7 - x % 8)))

display.show()
