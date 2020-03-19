from scipy.stats import norm
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
mu = 0
sigma = 1
x = np.arange(-5, -5, 0.1)
y = norm.ppf(x, mu, sigma)
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)
print(y)
plt.show()
