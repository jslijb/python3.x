#coding = utf-8
import pandas as pd
#将E:\\python\\Breast-Cancer\\breast-cancer-train.csv 文件的内容赋给df_train 这个变量，同时在前面添加了行号
#行号从0开始，导行这一行是计算行号的
df_train = pd.read_csv('E:\\python\\Breast-Cancer\\breast-cancer-train.csv')
df_test = pd.read_csv('E:\\python\\Breast-Cancer\\breast-cancer-test.csv')
#将文件E:\\python\\Breast-Cancer\\breast-cancer-test.csv  筛选Type 列为0 只取Clump Thickness 和 Cell Size
#这两列，并在前面添加行号，行号同样是从0开始，导行这一行是不计算行号的，将这个二维表赋值给df_test_negative
#筛选Type 列为1，赋值给df_test_positive
df_test_negative = df_test.loc[df_test['Type'] == 0] [['Clump Thickness','Cell Size']]
df_test_positive = df_test.loc[df_test['Type'] == 1] [['Clump Thickness','Cell Size']]
#matplotlib.pyplot 提供类似于MATLAB 绘图框架
import matplotlib.pyplot as plt
#scatter 这函数是画二维平面散点图，x,y轴
#scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None,
# linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)
#参数说明
#x 轴 一维数组，数组中的元素可以理解为x轴的坐标值
#y 轴 一维数组
#marker 标记，点，圆，到三角，正三角等 默认是'o' 实心圆
#s 表示标记的大小
#c 表示颜色 b=blue   c=cyan(青色)   m=magenta(品红)   r=red   w=white   y=yellow
#marker     描述
# "."               点，实行圆
# "o"               实心圆，比点要大
# ","               像素使用正方形表示和s一样
# "s"               正方形
# "v"               倒三角
# "^"               正三角
# "<"               左三角
# ">"               右三角
# "1"               三叉路口图标，像Y型，竖线向下
# "2"               三叉路口图标，竖线向上，想奔驰车图标
# "3"               三叉路口图标，竖线向左
# "4"               三叉路口图标，竖线向由
# "8"               八角形
# "p"               五边形
# "*"               五角星
# "h' 或者 'H'      六边形
# "+"               + 图标
# "x"               X 图片
# "d"               ◆ 菱形
# "D"               ◆ 菱形，粗些，图标大些
# "|"               管道符
# "_"               下划线
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'],marker = 'o',s=200,c='red')
#设置 x 轴标签和y轴标签
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
#显示图形
plt.show()
#numpy 数学运算库
import numpy as np
# np.random.random() 生成一个 [0.0 --- 1.0) 随机数，半开区间，意思就是有可能为0
#python3 生成一个精度为17位的小数 0.04163231487806429
# np.random.random(0) 和 np.random.random([0]) 等价 生产一个空是数组
# a = np.random.random(0) 生成一个空的 numpy.ndarray 数组  print (a) 输出：[]。交互界面之间输入a 输出array([], dtype=float64)
# type(a) 输出：numpy.ndarray
# b = np.random.random(1)  生成只有一个元素的列表 print(b) 输出 [ 0.314128]
# c = np.random.random(2)  生成只有2个元素的列表 print(c)  输出 [ 0.73122361  0.88214354]
# d = np.random.random(n)  n大于或等于0的整数 表示生成n个元素的列表，每个元素都是一个精度为8位的小数

intercept = np.random.random([1])
coef = np.random.random([2])
# lx = [0,1,2,3,4,5,6,7,8,9,10,11]
# intercept 类型 numpy.ndarray 可以理解为数学中的数字
# 两数组之间可以做相加，相减，相乘，相除等操作，但是要保证两数组之间的元素相同，或者是其中有一个数组只有一个元素
# 数组之间的相加，相乘，相除，相减 操作都是对应的元素相加，相乘，相除，相减，所得到的值组成一个新的数组
# l1 = np.random.random(2) [ 0.65064182  0.06834058]
# l2 = np.random.random(2) [ 0.04320734,  0.78783002]
# l1 + l2 = [ 0.69384916,  0.8561706 ]
# (0.65064182 + 0.04320734) = 0.69384916    (0.06834058 + 0.78783002) = 0.8561706
# l3 = np.random.random(3)
# l3 + l2  会报语法错误
# 相减，相乘，相除 操作原理一样
# l4 = np.random.random(1)   print(l4)  输出 [ 0.43167551]
# print (l4 + l1)  输出 [ 1.08231732,  0.50001609]
# 0.65064182 + 0.43167551 = 1.08231732    0.06834058 + 0.43167551 =  0.50001609
# l1 + l4 = l4 + l1
lx = np.arange(0,12)
ly = (-intercept - lx * coef[0]) / coef[1]
# plot以lx为x轴坐标，ly为y轴坐标，画一条xy轴平面一条线,颜色为黄色
plt.plot(lx,ly,c='yellow')
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'],marker='o',s=200,c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'],marker='x',s=150,c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()

#LogisticRegression 这个库包含逻辑回归
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
#fit 函数对样本数据进行训练
lr.fit(df_train[['Clump Thickness','Cell Size']][:10],df_train['Type'][:10])
print ('Testing accuracy(10 tranining samples):',lr.score(df_test[['Clump Thickness','Cell Size']],df_test['Type']))
intercept = lr.intercept_
print('intercept: ',intercept)
coef = lr.coef_[0,:]
print('coef: ',coef)
ly = (-intercept -lx * coef[0]) / coef[1]
plt.plot(lx,ly,c='green')
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'],marker='o',s=200,c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'],marker='x',s=150,c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()
lr = LogisticRegression()
lr.fit(df_train[['Clump Thickness','Cell Size']],df_train['Type'])
print ('Test accuracy(all training samples):',lr.score(df_test[['Clump Thickness','Cell Size']],df_test['Type']))
intercept = lr.intercept_
coef = lr.coef_[0,:]
ly = (-intercept -lx * coef[0]) / coef[1]
plt.plot(lx,ly,c='blue')
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'],marker='o',s=200,c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'],marker='x',s=150,c='black')
plt.xlabel('Clump Thickness')
plt.xlabel('Cell Size')
plt.show()