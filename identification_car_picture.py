'''
将一个文件夹下的所有车牌照都识别出来，并存入car_plate列表
'''


from hyperlpr import *
import os
#导入OpenCV库
import cv2

picture_root_path="../picture"
car_plate=[]
for filename in os.listdir(picture_root_path):
    picture_path=picture_root_path + "/" + filename
    image = cv2.imread(picture_path)
    res = HyperLPR_PlateRecogntion(image)
    car_plate.append(res[0][0])

print(car_plate)