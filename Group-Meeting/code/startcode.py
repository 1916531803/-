# @Author  : Harrison
# @Time   : 2023/12/7 21:02
# @Function:多线程编码
import threading
import subprocess
import os

# 定义要执行的.bat文件的目录列表
# directories = [
#     "C:/Users/Harrison/Desktop/GEO/data/bikes_19_eslf",
#     "C:/Users/Harrison/Desktop/GEO/data/IMG_1306_eslf",
#     # 添加更多目录...
# ]
path="C:/Users/Harrison/Desktop/GEO/data/test"
directories=[]
path_list = os.listdir(path)
for file in path_list:
    filePath = os.path.join(path, file)
    directories.append(filePath)
def execute_bat_files(dir_path):
    # 获取目录下所有文件和文件夹的列表
    files_list = os.listdir(dir_path)

    # 对文件列表进行排序
    sorted_files_list = sorted(files_list)

    # 遍历排序后的文件列表
    for file in sorted_files_list:
        # 获取文件的完整路径
        file_path = os.path.join(dir_path, file)

        # 判断文件是否为.bat文件
        if os.path.isfile(file_path) and file.endswith(".bat"):
            # 启动.bat文件，并显示命令行窗口
            subprocess.Popen(file_path, cwd=dir_path, shell=True).wait()


# 创建并启动线程
threads = []
for dir_path in directories:
    thread = threading.Thread(target=execute_bat_files, args=(dir_path,))
    thread.start()
    threads.append(thread)

# 等待所有线程执行完毕
for thread in threads:
    thread.join()
