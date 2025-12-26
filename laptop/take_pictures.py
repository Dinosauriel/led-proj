import time
import cv2
import subprocess
import config
import sys
import os
import shutil

def take_picture(camera, filename):
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        return

    # cv2.namedWindow("test")
    # cv2.imshow("test", frame)
    # cv2.waitKey(0)
    cv2.imwrite(filename, frame)


def main():
    n = int(sys.argv[1])
    print(f"number of leds: {n}")

    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out"
    if os.path.exists(out_path):
        print(f"out_path already exists: {out_path}")
        char = input("press y+[Enter] to delete existing out_path")
        if char == 'y':
            shutil.rmtree(out_path)
        else:
            print("aborting")
            return

    try:
        os.mkdir(out_path)
    except Exception as e: 
        print(f"Could not create directory: {e}")

    camera = cv2.VideoCapture(0)
    print("waiting for camera to adjust")
    time.sleep(0.5)
    print("done wating")

    for i in range(n):
        ssh_process = subprocess.Popen(["ssh", config.SERVER_SSH_HOSTNAME, f"sudo python3 {config.SERVER_PROJECT_PATH}/pi/single_light.py {i}\n".encode('utf-8')], stdin=subprocess.PIPE, stdout = subprocess.PIPE)
        ssh_process.communicate()
        print(f"taking picture no {i}")
        take_picture(camera, f"{out_path}/{i:04}.jpg")

    camera.release()

if __name__ == "__main__":
    main()
