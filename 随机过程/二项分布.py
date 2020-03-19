from scipy.stats import binom
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# rvs:对随机变量进行随机取值，可以通过size参数指定输出的数组的大小。
# pdf:概率密度函数
# cdf:分布函数。F(x)表示随机变量的取值<x<x 的概率。
# sf:随机变量的生存函数1-cdf(t)
# ppf:累积分布函数的反函数
# stat:计算随机变量的期望和方差
# fit:拟合，找到最适合取样数据的概率密度函数的系数。

## 设置属性防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
## 把画布分成几行几列
fig, ax = plt.subplots(1, 2)
n = 100
p = 0.3
# 平均值, 方差, 偏度, 峰度
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
print (mean, var, skew, kurt)
# ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
ax[0].plot(x, binom.pmf(x, n, p), 'o')
plt.title(u'二项分布概率质量函数')
plt.show()
