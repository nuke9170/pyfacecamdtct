import cv2
import keyboard
#pip3 install tk

face_cascade = cv2.CascadeClassifier()


#to cap video from webcam
cap = cv2.VideoCapture(0)
#to use a video file as input
# cap = cv2.VideoCapture('path to file here')


while not keyboard.is_pressed('esc'):
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
                                                            
    cv2.imshow('img',img)
    k= cv2.waitKey(30) & 0xff
    if k==27: break

cap.release()   