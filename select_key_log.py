# -*- coding:utf-8 -*-

import chardet
log = open("C:\\Users\\ljb\\Downloads\\catalina.2017-10-18.out",'rb')
data = log.read()
print(chardet.detect(data))
# for line in log: