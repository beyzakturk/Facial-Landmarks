# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:26:04 2022

@author: Beyza
"""

import cv2
import dlib

cap = cv2.VideoCapture("images-videos/elon_musk.mp4")

while True:
    
    ret,frame = cap.read()
    if ret == False:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    color = (0,0,255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("dataset/shape_predictor_81_face_landmarks.dat")
    
    faceLocs = detector(frame) #Yüzün konumlarını verir.
    
    for index, faceLoc in enumerate(faceLocs):
        landmarks = predictor(gray, faceLoc)
        for i in range(0,81):
            x= landmarks.part(i).x
            y= landmarks.part(i).y
            cv2.putText(frame, str(i), (x,y), font, .3, color,1,cv2.LINE_AA)
            cv2.circle(frame, x,y, 2, color, -1)
            
    cv2.imshow("Barack Obama", frame)        
    
    if cv2.waitKey(5) & 0xFF == ord("c"):
        break

cap.release()
cv2.destroyAllWindows()
    