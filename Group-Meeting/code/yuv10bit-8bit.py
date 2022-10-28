# @Author  : Harrison
# @Time   : 2022/7/28 13:15
# @Function编码后10bityuv转化为8bit
import os
from ffmpy3 import FFmpeg
import cv2
import numpy as np
height=512
width=512
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
    if not os.path.exists(savepath):
        os.mkdir(savepath)
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
#10bit转8bit
def rdb2yuv(inputPath,outpath,outname,RA):
    inputPath=inputPath+"/dec{}.yuv".format(outname+RA)

    resultName=outpath+"/dec"+outname+RA+"8bit.yuv"
    ff = FFmpeg(inputs={inputPath: '-s 512X512 -pix_fmt yuv420p10le'},
                outputs={resultName: '-pix_fmt yuv420p'})
    # print(ff.cmd)
    ff.run()
def main(imgpath,savepath,RA):
    for i in os.listdir(imgpath):

        savepath1=os.path.join(savepath,i)
        if not os.path.exists(savepath1):
            os.mkdir(savepath1)

        rdb2yuv(os.path.join(imgpath,i),os.path.join(imgpath,i),i,RA)
        eightbitName=os.path.join(imgpath,i+"/dec{}8bit.yuv".format(i+RA))
        YUVvideo2IMGs(eightbitName,os.path.join(savepath,i),height,width)
if __name__ == '__main__':
    RA="RA37"
    # imgpath='C:/Users/Harrison/Desktop/stanford/sampletest/BPP'
    imgpath ='C:/Users/Harrison/Desktop/HCI/decode/BPP/VVC'
    # savepath='C:/Users/Harrison/Desktop/HCI/decode/sampleZigZag/{}'.format(RA)
    # savepath = 'C:/Users/Harrison/Desktop/HCI/decode/LFRFNet/{}'.format(RA)
    savepath ='C:/Users/Harrison/Desktop/HCI/decode/BPP/VVC'
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    main(imgpath,savepath,RA)


