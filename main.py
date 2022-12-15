import argparse
import time
import config
import neopixel
import board
import importlib
import os
from controls.controls import XboxController

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help="name of the pattern to be displayed")
    parser.add_argument("-c", "--calibrate", choices=["server", "client"], help="mode to use for calibration. e.g. 'server' for raspberry pi, 'client' for laptop taking photos")
    parser.add_argument("-g", "--gencoords", help="generate the coords.csv file from image folder")
    return parser.parse_args()

def get_pattern(name):
    print("showing pattern " + name)
    try:
        mod = importlib.import_module("pattern_lib." + name)
        pattern = mod.Pattern(config.NUM_LEDS)
        return pattern
    except:
        print(f"couln't find pattern \"{name}\". make sure \"pattern_lib/{name}.py\" exists")

def main():
    args = get_args()
    controller = XboxController()

    if args.calibrate == "server":
        import calibrate_server
        print(f"running calibration as {args.calibrate}")
        calibrate_server.calibrate_server()
        return
    elif args.calibrate == "client":
        import calibrate_client
        print(f"running calibration as {args.calibrate}")
        calibrate_client.calibrate_client()
        return

    working_dir = os.path.dirname(os.path.realpath(__file__))
    pattern_files = [f[:-3] for f in os.listdir(working_dir + "/pattern_lib") if f[:2] != "__"] 
    print("available patterns: ", pattern_files)


    pixels = neopixel.NeoPixel(board.D18, config.NUM_LEDS, auto_write=False, pixel_order=neopixel.RGB, brightness=1.0)

    pattern_i = 0
    pattern = get_pattern(pattern_files[pattern_i])

    last_frame = 0
    while True:

        buttons = controller.poll_buttons()

        if buttons[controller.XBOX_A]:
            pattern_i = (pattern_i + 1) % len(pattern_files)
            pattern = get_pattern(pattern_files[pattern_i])
            last_frame = 0
        if buttons[controller.XBOX_HOME]:
            print("turning off")
            pixels.fill((0, 0, 0))
            pixels.show()
            exit()

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