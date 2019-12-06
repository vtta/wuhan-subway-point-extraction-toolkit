import argparse
import cv2
import numpy as np


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define lower and uppper limits of the color we wants to mask
# all colors other than white
lo = np.array([1, 0, 0])
hi = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lo, hi)
# Change it to black
image[mask > 0] = (0, 0, 0)

# grey rgb 100 100 100 => hsv 0 0 100
lo = np.array([0, 0, 99])
hi = np.array([0, 0, 101])
mask = cv2.inRange(hsv, lo, hi)
# Change it to black
image[mask > 0] = (0, 0, 0)

cv2.imwrite("result.png", image)
