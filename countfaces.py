import numpy as np
import cv2
import time


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
count = 0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) != 0:
    	print("face Detected")
    	#print ("Number of faces detected: " + str(faces.shape[0]))
    #cv2.imshow('img',img)
    #if ('Number of faces detected' == 2):
    #	break

    
    cv2.imwrite('captured faces/frame%d.jpg' % count, img)
    count = count +1

    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    

cap.release()
cv2.destroyAllWindows()