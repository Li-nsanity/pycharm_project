from scipy.stats import poisson
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
## 把画布分成几行几列
_lambda = 2
k = np.arange(0, 10)
possion = poisson.pmf(k, _lambda)
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(k, possion)
print(possion)
plt.show()

