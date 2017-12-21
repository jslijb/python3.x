# -*- coding:utf-8 -*-
# from functools import reduce

# def char2num(s):
#     d1 = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return d1[s]
#
# def fn(x,y):
#     return x * 10 + y
#
# s1 = '12345'
# # s_iterable = map(char2num,s1)
# # num = reduce(fn,s_iterable)
# # num = reduce(fn,map(char2num,s1))
#
# num = reduce(lambda x,y: x*10 + y,map(char2num,s1))
#
# print(type(num))
# print(num)

# CHAR_TO_FLOAT= {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}
#
# def str2float(s):
#     nums = map(lambda ch:CHAR_TO_FLOAT[ch],s)
#     # print(list(nums))
#     point = 0
#     def to_float(f,n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             print('n = -1 f:',f)
#             return f
#         if point == 0:
#             print('point = 0 f:',f)
#             print('point = 0 n:',n)
#             return f * 10 + n
#         else:
#             point = point * 10
#             print('else f:',f)
#             print('else n:',n)
#             return f + n / point
#     return reduce(to_float,nums,0.0)
#     # c = reduce(to_float,nums)
#     # return c
# s = '1'
# print('str to float:',str2float(s))
# print(type(str2float(s)))
# from goto import with_goto
# @with_goto
# def range(start,stop):
#     i = start
#     result = []
#
#     label .begin
#     if i == stop:
#         goto .end
#     result.append(i)
#     i += 1
#     goto .begin
#     label .end
#     return  result
#
# a = range(1,5)
# print(a)
import re
ip = '1.5.255.255'
def check_intel_ip(ip):
    '''检查ip地址是否可在互联网上使用'''
    #对ip地址格式进行最基本的检查，格式：四个数字以3个小数点分开，每个数字0-255
    pattern = re.match(r'\b([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.'
                       r'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){2}'
                       r'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b',ip,re.I)
    # 下面过滤不能在互联网上使用的地址
    pattern_c = re.match(r'^192\.168\..*',ip,re.I)
    pattern_b = re.match(r'^172\.(1[6-9]|2[0-9]|3[0-1]).*',ip,re.I)
    pattern_a = re.match(r'^10\..*',ip,re.I)
    pattern_d = re.match(r'^2(2[4-9]|3[0-9])\..*',ip,re.I)
    pattern_e = re.match(r'^2(4[0-9]|5[0-5])\..*',ip,re.I)
    pattern_127 = re.match(r'^127.*',ip,re.I)
    pattern_100 = re.match(r'^100\.64\..*',ip,re.I)
    pattern_169 = re.match(r'^169\.254\..*',ip,re.I)
    pattern_255 = re.match(r'\b.*\.255.255.255\b',ip,re.I)
    if pattern:
        if pattern_255:
            print(ip,'is a broadcast address')
        elif pattern_c:
            print(ip, 'is a C class private address')
        elif pattern_b:
            print(ip, 'is a B class private address')
        elif pattern_a:
            print(ip,'is a A class private address')
        elif pattern_d:
            print(ip,'is a D class multicast address')
        elif pattern_e:
            print(ip,'is a E class reserved address')
        elif pattern_127:
            print(ip,'is a local loop test address ')
        elif pattern_100:
            print(ip,'is a telecom operator reserved address')
        elif pattern_169:
            print(ip,'is a local reserved address')

        else:
            #print(ip,'is a normal Internet address')
            return ip
    else:
        print("The ip format is error")



