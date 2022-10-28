# @Author  : Harrison
# @Time   : 2022/7/31 21:31
# @Function:解码后的视图取出用于重建
import os
import cv2
import shutil

def copy_dir(src_path, target_path):
    if os.path.isdir(src_path) and os.path.isdir(target_path):
        filelist_src = os.listdir(src_path)
        for file in filelist_src:
            path = os.path.join(os.path.abspath(src_path), file)
            if os.path.isdir(path):
                path1 = os.path.join(os.path.abspath(target_path), file)
                if not os.path.exists(path1):
                    os.mkdir(path1)
                copy_dir(path, path1)
            else:
                with open(path, 'rb') as read_stream:
                    contents = read_stream.read()
                    path1 = os.path.join(target_path, file)
                    with open(path1, 'wb') as write_stream:
                        write_stream.write(contents)
        return True

    else:
        return False

def HCI(path1,path2):
    for file in os.listdir(path2):
        listfile1 = os.path.join(path1, file)
        listfile2 = os.path.join(path2, file)
        if not os.path.exists(listfile1):
            os.mkdir(listfile1)

        # for b in range(2):
        #
        #     if (b==0):

        img = cv2.imread(listfile2 + "/f_b_"+ str('{:03d}'.format(1)) + ".png")
        cv2.imwrite(listfile1 + "/result_4_4" + ".png", img)
        img = cv2.imread(listfile2 +  "/f_b_"+ str('{:03d}'.format(2)) + ".png")
        cv2.imwrite(listfile1 +  "/result_4_10" + ".png", img)
    # if(b==1):
        img = cv2.imread(listfile2 + "/f_b_" + str('{:03d}'.format(3)) + ".png")
        cv2.imwrite(listfile1 + "/result_10_4" + ".png", img)
        img = cv2.imread(listfile2 + "/f_b_" + str('{:03d}'.format(4)) + ".png")
        cv2.imwrite(listfile1 + "/result_10_10" + ".png", img)

if __name__ == '__main__':
    RA="RA32"
    inputpath = r"C:/Users/Harrison/Desktop/GroupMeeting/Stanford/decode"
    savepath = r"C:/Users/Harrison/Desktop/GroupMeeting/Stanford/reconstruction"

    src_path=r"C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sample"
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    copy_dir(src_path,savepath)

    HCI(savepath, inputpath)
