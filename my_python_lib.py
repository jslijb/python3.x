# -*- coding:utf-8 -*-
# 这个文件存放个人写的一些简单的python代码来实现各种功能
import re
__all__ = ['list_all_element_multiplication','num','Test']
# 实现列表中所有的函数相乘
from functools import reduce
def list_all_element_multiplication (list_par):
    return reduce(lambda x,y: x * y,list_par)

num = 100
class Test():
    pass

# 幂运算 x^n 只需要x,n 为int或者float类型，不管x,n 是否为正负数
# 写此函数的用意在于练习raise TypeError 这个异常处理
# 此函数还包含一个知识点就是默认参数，如果不给定n的值，默认就是x^2
def custom_power_product(x,n=2):
    if not isinstance(x,(float,int)):
        raise TypeError('The type of x must be float or int')
    if not isinstance(n,(float,int)):
        raise TypeError('The type of n must bu float or int')
    # if n < 0 :
    #     raise ValueError('The value of n must be positive integer')
    p = 1
    # while n > 0:
    #     p = p * x
    #     n = n -1
    # return p
    return x ** n

# 计算阶乘函数 fact1(n),fact2(n) fact1(n)的性能要稍微好些，两者的运行效率都不错
def fact1(n):
    if n < 0:
        raise ValueError('The value of n must be greater than 0')
    if n == 1:
        return 1
    if not isinstance(n,(int,)):
        raise TypeError('The type of n must be int')
    i = 1
    factorial = 1
    while i <= n:
        factorial = factorial * i
        i += 1
    return factorial

def fact2(n):
    if n < 0:
        raise ValueError('The value of n must be greater than 0')
    if n == 1:
        return 1
    if not isinstance(n,(int,)):
        raise TypeError('The type of n must be int')
    return n * fact2(n-1)


# 求列表中元素的最大值和最小值
# 第一种方法是将最大值和最小值分开求，这样写代码要复杂些，但是运行的效率要略高，
def find_max_element(L):
    max_element = L[0]
    i = 1
    while i < len(L):
        if max_element < L[i]:
            max_element = L[i]
        i += 1
    print('The largest element in this list: ',max_element)

def find_min_element(L):
    min_element = L[0]
    for i in L[1:]:
        if i < min_element:
            min_element = i
    print('The smallest element in this list: ', min_element)


def check_intel_ip(ip):
    '''检查ip地址是否可在互联网上使用'''
    # 对ip地址格式进行最基本的检查，格式：四个数字以3个小数点分开，每个数字0-255
    pattern = re.match(r'\b([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.'
                       r'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){2}'
                       r'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b', ip, re.I)
    # 下面过滤不能在互联网上使用的地址
    pattern_c = re.match(r'^192\.168\..*', ip, re.I)
    pattern_b = re.match(r'^172\.(1[6-9]|2[0-9]|3[0-1]).*', ip, re.I)
    pattern_a = re.match(r'^10\..*', ip, re.I)
    pattern_d = re.match(r'^2(2[4-9]|3[0-9])\..*', ip, re.I)
    pattern_e = re.match(r'^2(4[0-9]|5[0-5])\..*', ip, re.I)
    pattern_127 = re.match(r'^127.*', ip, re.I)
    pattern_100 = re.match(r'^100\.64\..*', ip, re.I)
    pattern_169 = re.match(r'^169\.254\..*', ip, re.I)
    pattern_255 = re.match(r'\b.*\.255.255.255\b', ip, re.I)
    if pattern:
        if pattern_255:
            print(ip, 'is a broadcast address')
        elif pattern_c:
            print(ip, 'is a C class private address')
        elif pattern_b:
            print(ip, 'is a B class private address')
        elif pattern_a:
            print(ip, 'is a A class private address')
        elif pattern_d:
            print(ip, 'is a D class multicast address')
        elif pattern_e:
            print(ip, 'is a E class reserved address')
        elif pattern_127:
            print(ip, 'is a local loop test address ')
        elif pattern_100:
            print(ip, 'is a telecom operator reserved address')
        elif pattern_169:
            print(ip, 'is a local reserved address')

        else:
            # print(ip,'is a normal Internet address')
            return ip
    else:
        print("The ip format is error")