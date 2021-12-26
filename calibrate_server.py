import neopixel
import board
import config

def calibrate_server():
    pixels = neopixel.NeoPixel(board.D18, config.NUM_LEDS)
    pixels.fill((0, 0, 0))

    for dim in range(2):
        for i in range(config.NUM_LEDS):
            input("press enter to continue...")
            print(f"led {i} of {config.NUM_LEDS}")
            pixels.fill((0, 0, 0))
            pixels[i] = (255, 255, 255)
    print("done!")


