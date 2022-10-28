# @Author  : Harrison
# @Time   : 2022/4/23 16:08
# @Function:批量计算SSIM,PSNR

# import the necessary packages
import math

import skimage
from skimage.metrics import structural_similarity as ssim, structural_similarity
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from skimage.measure import compare_ssim
def mse(imageA, imageB):
    # 均方误差方法用 python实现
    # 计算俩张图片的像素差的平方和的平均值
    # 俩张图必须有相同的 分辨率维度
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
def bgr2ycbcr(img, only_y=True):
    '''same as matlab rgb2ycbcr
    only_y: only return Y channel
    Input:
        uint8, [0, 255]
        float, [0, 1]
    '''
    in_img_type = img.dtype
    img.astype(np.float32)
    if in_img_type != np.uint8:
        img *= 255.
    # convert
    if only_y:
        rlt = np.dot(img, [24.966, 128.553, 65.481]) / 255.0 + 16.0
    else:
        rlt = np.matmul(img, [[24.966, 112.0, -18.214], [128.553, -74.203, -93.786],
                              [65.481, -37.797, 112.0]]) / 255.0 + [16, 128, 128]
    if in_img_type == np.uint8:
        rlt = rlt.round()
    else:
        rlt /= 255.
    return rlt.astype(in_img_type)


def compt_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 1.0

    if mse > 1000:
        return -100
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def compare_images(imageA, imageB, title):
    # 计算俩张图片的均方误差 及 结构相似性指数
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    # 设置图片的名称标头
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # 展示第一张图
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # 展示第二张图
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # 展示图片
    plt.show()

def ssimcute(imageA, imageB):
    # 计算俩张图片的均方误差 及 结构相似性指数
    s = ssim(imageA, imageB)
    return s

def caculateSSIMPSNR(imgpath1,imgpath2):

    listSSIMPSNR=[]
    SumSSIM=0
    SumPSNR=0
    for file in  os.listdir(imgpath1):
        # print(file)
        if(file.endswith('.yuv')):
            continue
        else:
            original = cv2.imread(os.path.join(imgpath1,file))
            contrast = cv2.imread(os.path.join(imgpath2,file))
            # original=bgr2ycbcr(original)
            # contrast=bgr2ycbcr(contrast)
            # print(original.dtype)
            # print(contrast.dtype)

            SSIM = ssim(original, contrast,multichannel=True)
            SumSSIM+=SSIM
            # psnr=compt_psnr(original,contrast)
            psnr = skimage.measure.compare_psnr(original,contrast, 255)
            SumPSNR+=psnr
            listSSIMPSNR.append("SSIM:"+str(SSIM)+"   "+"PSNR:"+str(psnr))

    print(listSSIMPSNR)
    filetxt = open(imgpath2 + "/SSIMPSNR.txt", 'w')
    num=1
    for i in listSSIMPSNR:
        filetxt.write("第{}张图对比结果:".format(num)+i)
        filetxt.write('\n')
        num=num+1
    filetxt.write("平均SSIM:"+str(SumSSIM/16)+"平均psnr:"+str(SumPSNR/16))

def main(imgpath1,imgpath2):
    for i in os.listdir(imgpath1):
        caculateSSIMPSNR(os.path.join(imgpath1,i),os.path.join(imgpath2,i))

if __name__ == "__main__":
    imgpath1 = "C:/Users/Harrison/Desktop/sampletest/sampleSampleZigzag"
    imgpath2 = "C:/Users/Harrison/Desktop/decode/SampleZigZagRA32"
    main(imgpath1,imgpath2)
