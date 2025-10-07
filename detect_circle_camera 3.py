from picamera.array import PiRGBArray
from picamera import PiCamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time, cv2, sys, imutils, cv

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (400, 300)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(400, 300))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    img   = cv2.medianBlur(image, 3)
    imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #imgg  = cv2.blur(imgg, (3,3))
    #imgg = cv2.dilate(imgg, np.ones((5, 5)))
    #imgg = cv2.GaussianBlur(imgg,(5,5),0)
    contours = cv2.findContours(Canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]

    cv2.imshow("Frame", imgg)

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    key = cv2.waitKey(1) & 0xFF    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    if circles is None:
        continue        

    #Loop through my contours to find rectangles and put them in a list, so i can view them individually later.
    cntrRect = []
    for i in contours:
        epsilon = 0.05*cv2.arcLength(i,True)
        approx = cv2.approxPolyDP(i,epsilon,True)
        if len(approx) == 4:
            cv2.drawContours(roi,cntrRect,-1,(0,255,0),2)
            cv2.imshow('Roi Rect ONLY',roi)
            cntrRect.append(approx)
