# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:02:27 2022

@author: Beyza
"""

import cv2
import dlib

image = cv2.imread("images-videos/Barack_Obama.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

color = (0,0,255)
font = cv2.FONT_HERSHEY_SIMPLEX

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("dataset/shape_predictor_81_face_landmarks.dat")

faceLocs = detector(image) #Yüzün konumlarını verir.

for index, faceLoc in enumerate(faceLocs):
    landmarks = predictor(gray, faceLoc)
    for i in range(0,81):
        x= landmarks.part(i).x
        y= landmarks.part(i).y
        cv2.putText(image, str(i), (x,y), font, .3, color,1,cv2.LINE_AA)
        cv2.circle(image, x,y, 2, color, -1)
        
cv2.imshow("Barack Obama", image)        