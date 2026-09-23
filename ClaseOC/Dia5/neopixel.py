import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
try:
    pixels [0] = (255,0,0)
    pixels.show()
except KeyboardInterrupt:
    pixels [0] = (0,0,0)
    pixels.show()
