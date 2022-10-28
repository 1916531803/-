# @Author  : Harrison
# @Time   : 2022/7/11 21:22
# @Function:
import os
import cv2
import numpy as np
from typing import List

height=368
width=536

def YUVvideo2IMGs(file, savepath, height, width ):
    """
    Convert the YUV video to RGB images and save the images at the target folder
    Args:
        file: input yuv file name
        savepath: save path of each RGB images
        height: height of images
        width: width of images
    Returns:
     """
    img_size = int(width * height * 3 / 2)
    frames = int(os.path.getsize(file) / img_size)
    with open(file, "rb") as f:
        for frame_idx in range(frames):
            yuv = np.zeros(shape=img_size, dtype='uint8', order='C')
            for j in range(img_size):
                yuv[j] = ord(f.read(1))
            img = yuv.reshape((height * 3 // 2, width)).astype('uint8')
            bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_I420)
            if bgr_img is not None:
                cv2.imwrite(os.path.join(savepath, "f_b_%03d.png" % (frame_idx+1)), bgr_img)


def main(imgpath,savepath,RA):
    for i in os.listdir(imgpath):
        # if(i=="hevc"):
        savepath1 = os.path.join(savepath, i)
        if not os.path.exists(savepath1):
            os.mkdir(savepath1)

        # eightbitName=os.path.join(imgpath,i+"/dec{}.yuv".format(i+RA))
        eightbitName = os.path.join(imgpath, i + "/{}.yuv".format(i))
        YUVvideo2IMGs(eightbitName,os.path.join(savepath,i),height,width)


if __name__ == '__main__':
    RA="RA37"
    imgpath='C:/Users/Harrison/Desktop/GroupMeeting/Stanford/encodeReorder'
    savepath='C:/Users/Harrison/Desktop/GroupMeeting/Stanford/decode'
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    main(imgpath,savepath,RA)