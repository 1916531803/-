# @Author  : Harrison
# @Time   : 2022/8/7 10:56
# @Function:指定像素区域裁剪并将裁剪区域在原图标注

import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from PIL import Image
from PIL import ImageDraw
path = "C:/Users/Harrison/Desktop/resizemap/Aloe/our"  # 图像读取地址
savepath = "C:/Users/Harrison/Desktop/resizemap/Aloe/our"  # 图像保存地址
filelist = os.listdir(path)  # 打开对应的文件夹
total_num = len(filelist)  # 得到文件夹中图像的个数
# print(total_num)


for filename in os.listdir(path):
    # print(filename)  # 仅仅是为了测试
    if(filename=="7.png"):
        img = cv2.imread(path + "/"+filename)

        #
        # crop = img[60:230,100:210,:]  # [x:y,a:b,Z]x:开始的纵坐标，y:介绍纵坐标，Z:通道
        # crop1= img[70:151, 150:231, :]
        # crop2 = img[200:261, 420:481, :]
        # crop1 = img[120:170, 20:110, :]
        # cv2.imwrite(savepath + filename, crop1)  #####保存图片#########
        # cv2.rectangle(img, (100, 60), (210, 230), (0, 255, 0), 2)
        # img1=cv2.rectangle(img, (150, 70), (230, 150), (0, 0, 255), 1)
        # img1 = cv2.rectangle(img, (420, 200), (480, 260), (0, 255, 0), 1)
        #IMG_1541
        # img1 = cv2.rectangle(img, (20, 110), (110, 180), (0, 0,200), 1)
        # img1 = cv2.rectangle(img1, (20, 200), (110, 270), (200, 0, 0), 1)
        # crop1 = img[110:181, 20:111, :]
        # crop2 = img[200:271, 20:111, :]
        # Aloe
        img1=cv2.rectangle(img, (120, 70), (210, 140), (0, 0, 200), 1)
        img1 = cv2.rectangle(img, (420, 200), (510, 270), (200, 0, 0), 1)
        crop1 = img[200:271, 420:511, :]
        crop2 = img[70:141, 120:211, :]

        #bicycle
        # img1 = cv2.rectangle(img, (350, 110), (440, 180), (0, 0, 200), 1)
        # img1 = cv2.rectangle(img1, (335, 395), (425, 465), (200, 0, 0), 1)
        # crop1 = img[110:181, 350:441, :]
        # crop2 = img[395:466, 335:426, :]


        cv2.imwrite(savepath + "/crop1.png", crop1)
        cv2.imwrite(savepath + "/crop2.png", crop2)
        # cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        # x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
        # cv2.imwrite(savepath + filename, crop1)  #####保存图片#########
        cv2.imwrite(savepath + "/img.png", img1)  #####保存图片#########
        cv2.imshow('img', img)  #####显示图片#######

        cv2.imshow('crop', crop1)
        cv2.imshow('crop', crop2)
        cv2.waitKey(0)
        # 打开图片并根据坐标画框，并保存图片+显示
        # img = Image.open(path + "/"+filename)  # 打开图片
        # a = ImageDraw.ImageDraw(img)  # 用a来表示
        # crop1 = img[70:150, 130:210, :]
        # crop2 = img[200:420, 260:480, :]
        # cv2.imwrite(savepath + "/crop1.png", crop1)  #####保存图片#########
        # cv2.imwrite(savepath + "/crop2.png", crop2)
        # # 在边界框的两点（左上角、右下角）画矩形，无填充，边框红色，边框像素为5
        # a.rectangle(((150, 70), (210, 130)), fill=None, outline='red', width=2)
        # a.rectangle(((420, 200), (480, 260)), fill=None, outline='blue', width=2)
        # img.save("2.jpg")
        # image = os.path.join(os.getcwd(), '2.jpg')
        # img = cv2.imread(image)
        # cv2.imshow('image', a)
        # cv2.waitKey(0)

