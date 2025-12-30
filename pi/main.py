import argparse
import time
import config
import neopixel
import board
import importlib
import os
from controls.controls import XboxController
from pattern import Pattern1D, Pattern3D
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help="start with pattern")
    parser.add_argument("-c", "--coords", help="path to coordinates file")
    return parser.parse_args()

def get_pattern(name, coords=None):
    print("showing pattern " + name)
    try:
        mod = importlib.import_module("pattern_lib." + name)
        if issubclass(mod.Pattern, Pattern3D):
            print(f"{name} is 3D")
            pattern = mod.Pattern(config.NUM_LEDS, coords)
        else:
            print(f"{name} is 1D")
            pattern = mod.Pattern(config.NUM_LEDS)
        return pattern
    except Exception as e:
        print(f"couln't find or load pattern \"{name}\". make sure \"pattern_lib/{name}.py\" exists")
        print(e)


def main():
    args = get_args()
    print(args)

    coords = None
    if args.coords:
        coords = np.loadtxt(args.coords)
        print(f"read coordinates for {len(coords)} lights")


    controller = XboxController()

    working_dir = os.path.dirname(os.path.realpath(__file__))
    pattern_files = [f[:-3] for f in os.listdir(working_dir + "/pattern_lib") if f[:2] != "__"] 
    print("available patterns: ", pattern_files)
    if args.pattern:
        pattern_i = pattern_files.index(args.pattern)
    else:
        pattern_i = 0
    pattern = get_pattern(pattern_files[pattern_i], coords)

    pixels = neopixel.NeoPixel(board.D18, config.NUM_LEDS, auto_write=False, pixel_order=neopixel.RGB, brightness=1.0)

    last_frame = 0
    sleep = False
    while True:

        buttons = controller.poll_buttons()

        if sleep:
            if buttons[controller.XBOX_HOME]:
                print("waking up")
                sleep = False
                continue
            time.sleep(0.2)
            continue

        if buttons[controller.XBOX_HOME]:
            print("sleeping")
            pixels.fill((0, 0, 0))
            pixels.show()
            sleep = True
            continue

        if buttons[controller.XBOX_A]:
            pattern_i = (pattern_i + 1) % len(pattern_files)
            pattern = get_pattern(pattern_files[pattern_i], coords)
            last_frame = 0

        t = int(time.time() * 1000)
        if t - last_frame >= pattern.interval:
            last_frame = t
            pixels[:] = pattern.draw(t)
            pixels.show()
        time.sleep(0.0005)

    print("no command issued. exiting")
    return

if __name__ == "__main__":
    main()
