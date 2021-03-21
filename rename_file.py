#encoding:utf-8
# 这个程序就是每天23:00 把a目录下的所有今天的文件拷贝到b下以明天命名的文件夹下
# 因为指定a目录为源文件，不用配置文件输入就不用更改了

import os
import time
import datetime
import threading

import configparser

config = configparser.ConfigParser()
config.read("..\\create_file\\config.ini")

# "获取配置文件的path"
new_path =config.get("path","new_path")
source_path =config.get("path","source_path")



# 获取当前8位数时间
today_time_str = time.strftime("%Y%m%d",time.localtime())
tomorow_time_str= str(int(today_time_str)-1)
f = os.listdir(source_path)
# 创建需要的文件夹
folder = os.path.exists("D:\\b\\{}".format(tomorow_time_str))
if not folder:
    os.makedirs("D:\\b\\{}".format(tomorow_time_str))

new_path ="D:\\b\\{}".format(tomorow_time_str)

def func():
    timer = threading.Timer(86400, func)
    timer.start()
    n = 0
    for i in f:
        # 获取要原始文件地址+名
        oldname = source_path + f[n]
        print(f[n], type(f[n]))

        new_name = f[n].replace("20210320", tomorow_time_str)  # 此处是变成要更改的名

        newname = new_path + "{}".format(new_name)
        os.rename(oldname, newname)
        # print(oldname, "=======>", newname)
        n += 1


# 获取现在时间
now_time = datetime.datetime.now()
# 获取明天时间
today = now_time + datetime.timedelta()
year = today.date().year
month = today.date().month
day = today.date().day
# 获取23点
start_time = datetime.datetime.strptime(str(year) + "-" + str(month) + "-" + str(day) + " 23:00:00","%Y-%m-%d %H:%M:%S")
# 距离指定时间还有多久执行
timer_start_time = (today - start_time).total_seconds()
timer = threading.Timer(timer_start_time, func)
timer.start()