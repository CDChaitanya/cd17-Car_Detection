# CAR DETECTION

import cv2
import time 
import numpy as np

# CREATING car CLASSIFIER
car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')

# INITIATING VIDEO CAPTURING FROM A VIDEO
cam = cv2.VideoCapture('cars.avi')

while cam.isOpened():
    time.sleep(.1)
    
    # READING THE FRAME
    _,frame = cam.read()
    #frame = cv2.resize(frame , None , fx=0.5 , fy=0.5 , interpolation = cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    # PASSING GRAY FRAME TO BODY CLASSIFIER
    cars = car_classifier.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=3)
    
    # EXTRACTING BOUNDING BOXES FOR ANY BODIES IDENTIFIED
    for(x,y,w,h) in cars:
        cv2.rectangle(img=frame, pt1=(x,y), pt2=(x+w , y+h), color=(0,255,255), thickness=2)
        cv2.imshow('CAR DETECTION' , frame)
    
    if cv2.waitKey(1)==13:
        break

cam.release()
cv2.destroyAllWindows()
    
    