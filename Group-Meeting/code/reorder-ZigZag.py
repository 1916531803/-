# @Author  : Harrison
# @Time   : 2022/7/27 14:46
# @Function:对8x8的视图ZigZag排序
import os
import shutil

# 遍历更改文件名
def stanford(path1,path2):
    for listfile in os.listdir(path1):
        print(listfile)
        # if(listfile=="bikes"):
        savepath = os.path.join(path2, listfile)
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        num = 1
        for i in range(7):
            for j in range(7):
                file="result_{}_{}".format(i+4, j+4) + ".png"
                oringnal=os.path.join(path1,listfile,file)
                name = num
                # print(name)
                shutil.copy(oringnal,savepath+ "/f_b_" + str('{:03d}'.format(num)) + ".png")
                num=num+1


def HCI(path1,path2):
    for listfile in os.listdir(path1):
        savepath = os.path.join(path2, listfile)
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        num = 1
        saveNum=1
        for i in range(8):
            skip = 1
            for j in range(8):
                if(skip==1 and i!=0):
                    num+=1
                file="input_Cam{:03d}".format(num) + ".png"
                oringnal=os.path.join(path1,listfile,file)
                name = num
                # print(name)
                shutil.copy(oringnal,savepath+ "/f_b_" + str('{:03d}'.format(saveNum)) + ".png")
                num=num+1
                saveNum+=1
                skip+=1

if __name__ == '__main__':
    # 图片存放的路径
    path1 = r"C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sample"
    path2 = r"C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sampleReorder"
    if not os.path.exists(path2):
        os.mkdir(path2)
    stanford(path1,path2)