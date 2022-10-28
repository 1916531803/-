# @Author  : Harrison
# @Time   : 2022/7/28 11:25
# @Function:将多张图片转化成yuv格式
import os
from ffmpy3 import FFmpeg
def rdb2yuv(inputPath,outpath,outname):
    inputPath=inputPath+"/f_b_%3d.png"
    outname=outpath+"/"+outname+".yuv"
    ff = FFmpeg(inputs={inputPath:None},
                outputs={outname:'-s 536x368 -pix_fmt yuv420p'})
    ff.run()
def main(imgpath):
    for i in os.listdir(imgpath):
        if(i.endswith(".txt")):
            continue
        else:
            rdb2yuv(os.path.join(imgpath,i),os.path.join(imgpath,i),i)
if __name__ == '__main__':
    imgpath="C:/Users/Harrison/Desktop/GroupMeeting/Stanford/encodeReorder"
    main(imgpath)