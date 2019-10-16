from matplotlib import pyplot as plt
import numpy as np
import math

a1 = np.array([1, 2, 3])
c = np.array([3, 4, 5])
X1, Y1, Z1 = a1
X2, Y2, Z2 = c
plt.title('show data')
plt.scatter(X1, Y1, Z1, color="blue", label="a1")
plt.scatter(X2, Y2, Z2, color="red", label="a2")
def Mahalanobis(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    npvec = np.array([npvec1, npvec2])
    sub = npvec.T[0]-npvec.T[1]
    inv_sub = np.linalg.inv(np.cov(npvec1, npvec2))
    return math.sqrt(np.dot(inv_sub, sub).dot(sub.T))
def show_distance(exit_point, c):
    line_point = np.array([exit_point, c])
    x = (line_point.T)[0]
    y = (line_point.T)[1]
    o_dis = round(Mahalanobis(exit_point, c), 2)  # 计算距离,更改函数名称
    mi_x, mi_y = (exit_point+c)/2  # 计算中点位置，来显示“distance=xx”这个标签
    plt.annotate('distance=%s' % str(o_dis), xy=(mi_x, mi_y), xycoords='data', xytext=(+10, 0), textcoords='offset points', fontsize=10, arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=.2"))
    return plt.plot(x, y, linestyle="--", color='black', lw=1)
show_distance(a1, c)
plt.show()