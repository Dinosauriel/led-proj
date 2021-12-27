import argparse
import time
import patterns.gold as gold
import config
import neopixel
import board
import util
import importlib

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help="name of the pattern to be displayed")
    parser.add_argument("-c", "--calibrate", choices=["server", "client"], help="mode to use for calibration. e.g. 'server' for raspberry pi, 'client' for laptop taking photos")
    parser.add_argument("-g", "--gencoords", help="generate the coords.csv file from image folder")
    return parser.parse_args()



def main():
    args = get_args()

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

    if args.pattern != None:
        print(f"running pattern {args.pattern}")
        pixels = neopixel.NeoPixel(board.D18, config.NUM_LEDS, auto_write=False)

        try:
            mod = importlib.import_module("patterns." + args.pattern)
        except:
            print(f"couln't find pattern \"{args.pattern}\". make sure \"patterns/{args.pattern}.py\" exists")
            return

        pattern = mod.Pattern(config.NUM_LEDS)

        while not pattern.should_finish:
            t = int(time.time() * 1000)
            colors = pattern.draw(t)
            pixels[:] = [util.grb_to_rgb(c) for c in colors]
            pixels.show()
            time.sleep(0.05)

        return

    print("no command issued. exiting")
    return

if __name__ == "__main__":
    main()