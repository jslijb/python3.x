# -*- coding:utf-8 -*-
import re
prd1_nginx_log = open("C:\\Users\\ljb\\Downloads\\count_app_091.txt",'r')
prd2_nginx_log = open("C:\\Users\\ljb\\Downloads\\count_app_092.txt",'r')
prd_nginx_log = open("C:\\Users\\ljb\\Downloads\\count_app_09.txt",'w')
for line in prd1_nginx_log:
    # line = line.strip()
    prd_nginx_log.write(line)
for line in prd2_nginx_log:
    # line = line.strip()
    prd_nginx_log.write(line)
prd_nginx_log.close()
prd_nginx_log = open("C:\\Users\\ljb\\Downloads\\count_app_09.txt",'r')
nginx_log_list = prd_nginx_log.readlines()
prd1_nginx_log.close()
prd2_nginx_log.close()
prd_nginx_log.close()

i = 0
log_dict = {}
count = 0
while i < len(nginx_log_list):
    date = re.search('\d{8}',nginx_log_list[i].strip('\n')).group()
    log_dict.setdefault(date,[]).append(int(nginx_log_list[i+1].strip('\n')))
    i += 2
for key in log_dict:
    val = sum(log_dict[key])
    count += val
    print(key,'==>',float('%.2f' %(val/1024/1024)),'MB')
count= float('%.2f' %(count/1024/1024/1024))
key = re.search('\d{6}', key).group()
print(key,'==>',count,'GB')
