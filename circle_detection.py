from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import os
import numpy as np
os.system('sudo modprobe bcm2835-v4l2')

h=200
w=300
camera = PiCamera()
camera.resolution = (w, h)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(w, h))
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

image_RGB = frame.array
copy_RGB = image_RGB.copy() 
grey = cv2.cvtColor(image_RGB, cv2.COLOR_BGR2GRAY)

img_circles = None
img_circles = cv2.HoughCircles(grey, cv2.cv.CV_HOUGH_GRADIENT, 1, 2, 100)

if img_circles is not None:
    img_circles = np.round(img_circles[0, :]).astype("int")
    for (x, y, r) in img_circles:

        cv2.circle(copy_RGB, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(copy_RGB, (x - 5, y - 5),(x + 5, y + 5), (0, 128, 255, -1))

cv2.imshow("Copy with Detected Object", copy_RGB)

key = cv2.waitKey(1) & 0xFF
rawCapture.truncate(0)
if key == ord("q"):
    break