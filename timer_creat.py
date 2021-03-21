#encoding:utf-8
# 这个脚本为0点开始执行每隔15分钟从b目录拷贝相应的文件到所需要的目录
# 其中各个时间文件可做小修改
import datetime
import time
import threading
import shutil
import os

today_min_str = time.strftime("%Y%m%d%H%M",time.localtime())
today_day_str = time.strftime("%Y%m%d",time.localtime())
def func_task():
    new_folder = os.path.exists("D:\\b\\{}".format(today_day_str))
    if not new_folder:
        os.makedirs("D:\\b\\{}".format(today_day_str))
    shutil.copy("D\\b\\{}\\test{}.csv".format(today_day_str,today_min_str),"D\\c\\{}\\test{}.csv".format(today_day_str,today_min_str))


def func_timer():

    func_task()
    global timer
    # 15分钟拷贝一次当前符合时间的文件
    timer = threading.Timer(900, func_timer)

    timer.start()    #启用定时器


now_time = datetime.datetime.now()
# 获取明天0:0:0时间
tomorow = now_time + datetime.timedelta(days=+1)
year = tomorow.date().year
month = tomorow.date().month
day = tomorow.date().day
start_time = datetime.datetime.strptime(str(year) + "-" + str(month) + "-" + str(day) + " 00:00:00","%Y-%m-%d %H:%M:%S")
timer_start_time = (tomorow - start_time).total_seconds()
timer = threading.Timer(timer_start_time, func_timer)

timer.start()