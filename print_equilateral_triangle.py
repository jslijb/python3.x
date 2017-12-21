# -*- coding:utf-8 -*-
# 画等边三角形

# import turtle
# import time
# # length = 300
# # for i in range(0,3):
# #     turtle.seth(i*120)
# #     turtle.fd(length)
# #     time.sleep(5)
# # turtle.done()
#
# # 运行3次转向，4次移动 画成一个正方形
# # 创建一个画布
# t = turtle.Pen()
# # 从坐标原点(画布的中心)向左移动50个像素，默认是向左
# t.forward(50)
# time.sleep(3)
# # 画笔向左转90度
# t.left(90)
# t.forward(50)
# time.sleep(3)
# # 转90度和转270度效果一样
# # t.right(270)
# t.left(90)
# t.forward(50)
# time.sleep(3)
# t.left(90)
# t.forward(50)
# time.sleep(3)
# # t.clear()

# 打印倒等边三角形
line = int(input('please input line: '))
i = 1
a = '* '
total = line + (line - 1)
print(line * a)
while i < line:
    if i == line -1 :
        print((total // 2) * ' '+ '*' + (total //2)* ' ')
    else:
        print(i * ' '+'*'+(total - 2 - 2 * i) * ' '+'*')

    i = i + 1
