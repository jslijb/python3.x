# coding = utf-8
import time
import datetime
import os
#除周末外的法定节假日列表
lt1 = ['2017-10-02','2017-10-03','2017-10-04','2017-10-05','2017-10-06']
#周末调休列表
lt2 = ['2017-09-30']
date=time.strftime('%Y-%m-%d',time.localtime())
print('today is',date)
weekday=datetime.datetime.now().weekday()
print('What day is today',weekday)
#首先在周末调休列表，如果不在就判断不在节假日列表而且不是周末
#
if date in lt2:
    os.popen('shutdown /s')
if date not in lt1:
    if weekday !=5 and weekday != 6:
        os.popen('shutdown /s /t 360')
