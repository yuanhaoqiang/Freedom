#coding=utf-8
from hyperlpr import *
import os
#导入OpenCV库
import cv2


vip_number_txt_path="../vip_number_database/vip_car.txt"
vip_number_txt = open(vip_number_txt_path,encoding='utf-8')
vip_number_txt_list=[]

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

while 1:
    ret, frame = cap.read()
    cv2.imshow('cap', frame)

    res=HyperLPR_PlateRecogntion(frame)
    if res:
        final_res=res[0][0]

        if final_res in vip_number_txt_list:
            print('vip number:'+final_res)
        else:
            print('not vip number:'+final_res)

    if(cv2.waitKey(50) & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()