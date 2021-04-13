# install requirements
import cv2  # computer vision
import numpy as np
import time

print("""

Harry :  Hey !! Would you like to try my invisibility cloak ??

         Its awesome !!


         Prepare to get invisible .....................
    """)

cap = cv2.VideoCapture(1)  # start your default laptop camera
# 1,2 if you don't have a camera on your laptop
time.sleep(3)  # time to open cam
background = 0
for i in range(30):  # time to store image
    ret, background = cap.read()  # use loop to get precise image

background = np.flip(background, axis=1)  # flip image

while (cap.isOpened()):
    ret, img = cap.read()

    # Flipping the image (Can be uncommented if needed)
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Converting image to HSV color space
    # detect colours better
    value = (35, 35)

    blurred = cv2.GaussianBlur(hsv, value, 0)

    # Defining lower range for blue color detection.
    lower_blue = np.array([0, 0, 77])
    upper_blue = np.array([0, 0, 139])  # can be modified to any colour
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

    # Defining upper range for blue color detection
    lower_blue = np.array([0, 0, 77])
    upper_blue = np.array([0, 0, 139])
    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

    # Addition of the two masks to generate the final mask.
    mask = mask1 + mask2  # detect all ranges of Blue
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    # Replacing pixels corresponding to cloak with the background pixels.
    img[np.where(mask == 139)] = background[np.where(mask == 139)]
    cv2.imshow('Display', img)
    k = cv2.waitKey(10)
    if k == 27:
        break

# RUN IT!
# MAKE GOOD USE OF IT ;)
