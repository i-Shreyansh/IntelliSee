import cv2
import tensorflow as tf


#enter check 0 t0 5 for ur webcam
a=cv2.VideoCapture(0)


while True:
    sucess,img =a.read()
    cv2.imshow("video",img)
    if cv2.waitKey(20 ) & 0xFF == ord("q"):
        break

