from hyperlpr import *
import cv2
import os
import time

#image1 = cv2.imread("demo1.jpg")
#image2 = cv2.imread("demo_no.jpg")


#cv2.imshow("demo1.jpg", image1)
#cv2.imshow("demo_no.jpg", image2)
#os.system("pause")
#time.sleep(5)
cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    cv2.imshow('cap', frame)

    print(HyperLPR_PlateRecogntion(frame))
    if(cv2.waitKey(50) & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
