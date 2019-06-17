'''
该程序用于删除一个文件夹中所有无法识别的车牌号照片
'''


from hyperlpr import *
import os
#导入OpenCV库
import cv2

# 图片所在文件夹
root_path="../picture"
car_plate=[]

for filename in os.listdir(root_path):
    path=root_path + "/" + filename
    image = cv2.imread(path)
    res = HyperLPR_PlateRecogntion(image)
    if res:
        car_plate.append(res[0][0])
    else:
        os.remove(path)


print(car_plate)