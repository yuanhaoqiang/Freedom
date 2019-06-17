from hyperlpr import *
import cv2
import os
import time

image1 = cv2.imread("demo1.jpg")
image2 = cv2.imread("demo_no.jpg")


cv2.imshow("demo1.jpg", image1)
cv2.imshow("demo_no.jpg", image2)
#os.system("pause")
time.sleep(5)
print("demo1:" + str(HyperLPR_PlateRecogntion(image1)))
print("demo_no:" + str(HyperLPR_PlateRecogntion(image2)))
