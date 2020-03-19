from scipy.stats import poisson
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
_lamdba = 2
n = np.random.uniform(0, 100, _lamdba * 100)
n.sort()
sum = 0
for i in range(0, len(n)):
    x = n[i]
    y = np.random.uniform(0, 1)
    sum = sum + y
    dic = [(x, sum)]
    s = dict(dic)
    print(s)
