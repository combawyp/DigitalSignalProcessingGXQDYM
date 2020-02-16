'''
 一个差分方程，如下：
 y(n)-a*y(n-1) = x(n)
 初始状态，如下：
 y(-1) = 0
 当输入信号x为一个单位脉冲序列
 显示输出
'''

import numpy
import scipy.signal
import matplotlib.pyplot

# 输入信号= 单位脉冲序列
xn  = numpy.append(1, numpy.zeros(30))
print(xn)

# 初始条件
ys  = [1, 0, 0, 0]
# 差分方程序列
a   = 0.8
A   = [1, -a]
B   = [1]

# 计算输出
xi  = scipy.signal.lfiltic(B, A, ys)
print(xi)

yn  = scipy.signal.lfilter(B, A, xn, zi=xi)
print(yn)

# 构造显示的 x 轴刻度
n   = numpy.arange(0, len(yn[0]), 1, dtype=int)
print(n)

# 为了让输入输出在一个图里显示，扩展输入长度
xn_dis  = numpy.append(xn, numpy.zeros(len(yn[0])-len(xn)))
print(xn_dis)
# 使用 figure 函数给绘图命名
matplotlib.pyplot.figure('例 1.4.1')
# 使用 subplot 函数设置图的排列
matplotlib.pyplot.subplot(111)
# 使用 plot 函数绘制输出，标注方式 o
matplotlib.pyplot.plot(n, yn[0], '-o')
# 使用 plot 函数绘制输入，标注方式 x
matplotlib.pyplot.plot(n, xn_dis, '-x')
# 使用 show 函数显示
matplotlib.pyplot.show()

# EOF
