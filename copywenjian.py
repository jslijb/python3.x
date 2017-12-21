# coding = utf-8
import os
import shutil
import time
import re

alllist = os.listdir("C:\\Users\\ljb\\Downloads\\")
for i in alllist:
    a = i.strip()
    pattern = re.compile(r'hins2852765.*')
    match = pattern.match(a)
    if match:
        b = match.group()
    else:
        continue
    sourcefile = u'C:\\Users\\ljb\\Downloads\\' + b
    destfile = u'\\\\192.168.1.25\\e\\backuprds\\' + b
    print("sourcefile:" + sourcefile)
    print("destfile:" + destfile)
    print(time.strftime('%H:%M:%S', time.localtime()))
    print(os.path.exists(destfile))
    if os.path.exists(destfile):
        pass
    else:
        shutil.copyfile(sourcefile, destfile)
        print(time.strftime('%H:%M:%S', time.localtime()))
    if os.path.getsize(sourcefile) == os.path.getsize(destfile):
        os.remove(sourcefile)