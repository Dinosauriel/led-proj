import cv2
import subprocess

def take_picture(camera, filename):
    cv2.namedWindow("test")
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        return

    cv2.imshow("test", frame)
    cv2.waitKey(0)
    cv2.imwrite(filename, frame)
    print("{} written!".format(filename))

def calibrate_client():
    camera = cv2.VideoCapture(0)
    take_picture(camera, "images/image.png")
    camera.release()