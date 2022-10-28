# @Author  : Harrison
# @Time   : 2022/7/27 10:58
# @Function:采样为4张图进行Z字排序
import os
import cv2
import shutil
def stanford(path1,path2):
    for file in os.listdir(path1):
        listfile1=os.path.join(path1, file)
        listfile2=os.path.join(path2, file)
        print(listfile1)
        i = 4
        num = 1
        for b in range(2):
            k = 4
            for j in range(2):
                if (b == 1 and j==0):
                    i += 6
                if (j == 1):
                    k += 6
                oringnal=listfile1+ "/result_{}_{}".format(i, k) + ".png"
                print(oringnal)
                img=cv2.imread(oringnal)
                savepath=listfile2
                if not os.path.exists(savepath):
                    os.mkdir(savepath)

                # cv2.imwrite(savepath, img)
                shutil.copy(oringnal,savepath+ "/f_b_" + str('{:03d}'.format(num)) + ".png")
                num = num + 1

def HCI(path1,path2):
    for file in os.listdir(path1):
        listfile1=os.path.join(path1, file)
        savepath=os.path.join(path2, file)
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        num = 1
        for i in range(4):
            if(i==0):
                for j in [1,4,5,8]:
                    oringnal=listfile1+"/f_b_" + str('{:03d}'.format(j) + ".png")

                    img=cv2.imread(oringnal)

                    # cv2.imwrite(savepath, img)
                    shutil.copy(oringnal,savepath+ "/f_b_" + str('{:03d}'.format(num)) + ".png")
                    num+=1
            if (i == 1):
                for j in [25, 28, 29, 32]:
                    oringnal = listfile1 + "/f_b_" +str('{:03d}'.format(j) + ".png")

                    img = cv2.imread(oringnal)

                    # cv2.imwrite(savepath, img)
                    shutil.copy(oringnal, savepath + "/f_b_" + str('{:03d}'.format(num)) + ".png")
                    num += 1
            if (i == 2):
                for j in [33, 36, 37, 40]:
                    oringnal = listfile1 + "/f_b_" + str('{:03d}'.format(j) + ".png")

                    img = cv2.imread(oringnal)

                    # cv2.imwrite(savepath, img)
                    shutil.copy(oringnal, savepath + "/f_b_" + str('{:03d}'.format(num)) + ".png")
                    num += 1
            if (i == 3):
                for j in [57, 60, 61, 64]:
                    oringnal = listfile1 + "/f_b_" + str('{:03d}'.format(j) + ".png")
                    img = cv2.imread(oringnal)
                    # cv2.imwrite(savepath, img)
                    shutil.copy(oringnal, savepath + "/f_b_" + str('{:03d}'.format(num)) + ".png")
                    num += 1
if __name__ == '__main__':
    path1 = r"C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sample"
    path2 = r"C:/Users/Harrison/Desktop/GroupMeeting/Stanford/encodeReorder"
    if not os.path.exists(path2):
        os.mkdir(path2)
    stanford(path1, path2)