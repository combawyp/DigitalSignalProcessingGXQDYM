'''
@Author: W.Y.P.
@Date: 2020-2-1 16:04:34
@LastEditTime: 2019-11-28 17:17:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \DigitalSignalProcessingGXQDYM\Ex1_3_4.py
'''
 
'''
 一个平均滤波器的差分方程，如下：
 y(n)= 1/5*[x(n)+x(n-1)+x(n-2)+x(n-3)+x(n-4)]
 当输入信号x为一个序列，如下：
 x[0~15]= [0.6, 0.6, 0.6, 1.0, 0.6, 0.6, 0.6, 1.0,0.6, 0.6, 0.6, 1.0,0.6, 0.6, 0.6]
 显示输出
'''

import numpy
import scipy.signal
import matplotlib.pyplot

# 输入信号
x   = (0.6, 0.6, 0.6, 1.0, 0.6, 0.6, 0.6, 1.0,0.6, 0.6, 0.6, 1.0,0.6, 0.6, 0.6)
xn  = numpy.asarray(x)
print(xn)

# 根据差分方程来的单位脉冲响应 h(x)
h   = (0.2, 0.2, 0.2, 0.2, 0.2)
hn  = numpy.asarray(h)
print(hn)

# 计算卷积
yn  = scipy.signal.convolve(hn, xn)
print(yn)

# 构造显示的 x 轴刻度
n       = numpy.arange(0, len(yn), 1, dtype=int)
print(n)

# 为了让输入输出在一个图里显示，扩展输入长度
xn_dis  = numpy.append(xn, numpy.zeros(len(yn)-len(xn)))
print(xn_dis)
# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 1.3.4')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制输出，标注方式 o
matplotlib.pyplot.plot(n, yn, '-o')
# 使用 plot 函数绘制输入，标注方式 x
matplotlib.pyplot.plot(n, xn_dis, '-x')
# 使用 show 函数显示
matplotlib.pyplot.show()

# EOF
