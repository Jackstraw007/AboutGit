import time
dt = "Apr/1992/22"
#转换成时间数组
timeArray = time.strptime(dt, "%b/%Y/%d")
#转换成新的时间格式(20160505-20:28:54)
dt_new = time.strftime("%Y-%m-%d",timeArray)

##############################
#Asc.py
###
#来自git的修改
