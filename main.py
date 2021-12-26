import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help="name of the pattern to be displayed")
    parser.add_argument("-c", "--calibrate", choices=["server", "client"], help="mode to use for calibration. e.g. 'server' for raspberry pi, 'client' for laptop taking photos")
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
        return

    print("no command issued. exiting")
    return

if __name__ == "__main__":
    main()