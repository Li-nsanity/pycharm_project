import matplotlib.pyplot as plt
import numpy as np

# 矩阵绘图
m = np.random.rand(10,10)
print(m)
plt.imshow(m, interpolation='nearest', cmap=plt.cm.ocean)
plt.colorbar()
plt.show()