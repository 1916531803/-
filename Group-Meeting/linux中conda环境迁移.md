linux中conda环境迁移

```text
# 把虚拟环境 my_env 打包为 my_env.tar.gz
conda pack -n my_env

# -o 参数指定打包路径和名称，把虚拟环境 my_env 打包为 out_name.tar.gz
conda pack -n my_env -o out_name.tar.gz
conda pack --no-cache-dir -n pytorch310 -o/home/harrison/lfg.tar.gz
# 把某个特定路径的虚拟环境打包为 my_env.tar.gz
conda pack -p /explicit/path/to/my_env
```



linux

```text
# 创建目录 `my_env`，并将环境解压至该目录
mkdir -p my_env
tar -xzf lfg.tar.gz -C /home/shnu_ibdi/anaconda3/envs/lfg


# 使用python而不激活或修复前缀。
# 大多数 python 库可以正常工作，但需要处理前缀的部分将失败。
./my_env/bin/python

# 激活环境，同时这步操作会将路径 `my_env/bin` 添加到环境变量 path
source my_env/bin/activate

# 在环境中运行python
(my_env) $ python

# 从激活环境中清除前缀。
# 请注意，也可以在不激活环境的情况下运行此命令
# 只要机器上已经安装了某个版本的python。
(my_env) $ conda-unpack

# 此时，环境与您在此路径直接使用 conda 安装的环境完全相同。
# 所有脚本都应该工作正常。
(my_env) $ ipython --version

# 停用环境以将其从环境变量 path 中删除
(my_env) $ source my_env/bin/deactivate
```





[远程神器 screen命令的保姆级详解教程+举例_screen远程_每天都想躺平的大喵的博客-CSDN博客](https://blog.csdn.net/weixin_39925939/article/details/121033427)