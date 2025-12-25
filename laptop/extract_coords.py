import cv2
import glob
import os
import sys
import numpy as np

def cross(image, x, y):
    cv2.rectangle(image, (x, y - 10), (x, y + 10), (0, 0, 255), 2)
    cv2.rectangle(image, (x - 10, y), (x + 10, y), (0, 0, 255), 2)


def main():
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out"
    #files = glob.glob(out_path + "/**.jpg")
    #print(files)

    n = int(sys.argv[1])
    coords = np.zeros((n, 3))

    for i in range(n):
        filename = out_path + f"/{i:04}.jpg"
        print(filename)
        image = cv2.imread(filename)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(image.shape)

        brightest = np.unravel_index(np.argmax(image), image.shape)
        print(brightest)
        yb, xb = brightest
        coords[i] = [xb, yb, 0]

        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        cross(image, xb, yb)
        cv2.imshow(filename, image)
        cv2.waitKey(0)

    xmin = np.min(coords[:, 0])
    # xmax = np.max(coords[:, 0])
    ymin = np.min(coords[:, 1])
    # ymax = np.max(coords[:, 1])
    coords[:, 0] -= xmin
    coords[:, 1] -= ymin

    np.savetxt(out_path + "/coords.csv", coords, fmt="%1i")

if __name__ == "__main__":
    main()
