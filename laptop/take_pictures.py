import cv2
import subprocess
import config

def take_picture(camera, filename):
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        return

    # cv2.namedWindow("test")
    # cv2.imshow("test", frame)
    cv2.waitKey(0)
    cv2.imwrite(filename, frame)

def calibrate_client():
    ssh_process = subprocess.Popen(["ssh", config.SERVER_SSH_HOSTNAME], stdin=subprocess.PIPE, stdout = subprocess.PIPE)
    ssh_process.stdin.write("cd " + config.SERVER_PROJECT_PATH + "\n")
    ssh_process.stdin.write("python3 main.py -c server")

    for line in ssh_process.stdout:
        print(line)

    camera = cv2.VideoCapture(0)

    print("ready to start taking pictures")
    print("make sure the object is in frame")
    input("press enter to start...")

    for i in range(config.NUM_LEDS):
        print(f"led {i} of {config.NUM_LEDS}")
        ssh_process.stdin.write("\n")
        take_picture(camera, f"images/dim0/{i:05}.png")

    print("first set of pictures done")
    print("rotate object by 90 degrees without changing the frame")
    input("press enter to continue...")

    for i in range(config.NUM_LEDS):
        print(f"led {i} of {config.NUM_LEDS}")
        ssh_process.stdin.write("\n")
        take_picture(camera, f"images/dim1/{i:05}.png")

    camera.release()

    ssh_process.stdin.write("exit\n")
    ssh_process.stdin.close()