'''
用于向数据库中添加vip车牌号
'''

path="../vip_number_database/vip_car.txt"
file = open(path,'a')
while True:
    number_str=input("please input vip number(input 'q' to quit):")
    if(number_str=='q'):
        break
    else:
        file.write('\n'+number_str)
file.close()

