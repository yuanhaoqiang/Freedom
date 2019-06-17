#coding=utf-8
from hyperlpr import *
import os
#导入OpenCV库
import cv2

import RPi.GPIO as GPIO
import time
import datetime


vip_number_txt_path="../vip_number_database/vip_car.txt"
vip_number_txt = open(vip_number_txt_path,encoding='utf-8')
vip_number_txt_list=[]

log_path="../log.txt"


GPIO.setmode(GPIO.BCM)
#the 6th pin in the right
GPIO.setup(18, GPIO.OUT)        
GPIO.output(18, GPIO.LOW)
#the 8th pin in the right
GPIO.setup(23, GPIO.IN)

while True:
    line = vip_number_txt.readline()
    line = line.strip('\n')
    if line:
        vip_number_txt_list.append(line)
    else:
        break

vip_number_txt.close()
# 通过上面的步骤，将vip号码名单读取到vip_number_txt_list中

cap = cv2.VideoCapture(0)

old_final_res = ''

while 1:
    ret, frame = cap.read()
    cv2.imshow('cap', frame)

    #dont have car
    if GPIO.input(23) is GPIO.HIGH:
#        flag = 0
        old_final_res = ''
        GPIO.output(18, GPIO.LOW)
    elif GPIO.input(23) is GPIO.LOW:   #have car
        res=HyperLPR_PlateRecogntion(frame)
       # print(GPIO.input(23))
        if res:   #frist time 
            final_res=res[0][0]
            if (len(final_res) != 7) or final_res == old_final_res :
                continue
          #  flag = 1        #frist time flag
            old_final_res = final_res
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            log_txt = open(log_path,'a')
            
            if final_res in vip_number_txt_list:
                print(now_time + '\tvip number:' + final_res)
                log_txt.write('\n' + now_time + '\tvip number:' + final_res);
                GPIO.output(18, GPIO.HIGH)
             #   time.sleep(5)
              #  GPIO.output(18, GPIO.LOW)
                log_txt.close()
            else:
                print(now_time + '\tnot vip number:'+final_res)
                log_txt.write('\n' + now_time + '\tnot vip number:' + final_res);
                log_txt.close()
    

    if(cv2.waitKey(50) & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
