import neopixel
import board
import config
import sys

def single_light(i: int):
    pixels = neopixel.NeoPixel(board.D18, config.NUM_LEDS)
    pixels.fill((0, 0, 0))

    print(f"led {i} of {config.NUM_LEDS}")
    pixels[i] = (255, 255, 255)

single_light(int(sys.argv[1]))
