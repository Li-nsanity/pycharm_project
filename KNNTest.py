from matplotlib import pyplot as plt
import numpy as np
import math

# 定义四个点的坐标
a1 = np.array([1, 2])
a2 = np.array([2, 3])
b1 = np.array([3, 3])
b2 = np.array([3, 4])
c = np.array([2, 1])
# 四个点坐标分别赋值给X,Y
X1, Y1 = a1
X2, Y2 = a2
X3, Y3 = b1
X4, Y4 = b2
X5, Y5 = c
plt.title('show data')
plt.scatter(X1, Y1, color="blue", label="a1")
plt.scatter(X2, Y2, color="blue", label="a2")
plt.scatter(X3, Y3, color="red", label="b1")
plt.scatter(X4, Y4, color="red", label="b2")
plt.scatter(X5, Y5, color="orange", label="c")
plt.legend(loc='upper left') #图例的位置
plt.annotate(r'a1(1,1)', xy=(X1, Y1), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'a2(1,2)', xy=(X2, Y2), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'b1(3,3)', xy=(X3, Y3), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'b2(3,4)', xy=(X4, Y4), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# plt.show()
# 计算欧拉距离

def Euclidean(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    return math.sqrt(((npvec1-npvec2)**2).sum())
'''
# Manhattan_Distance,曼哈顿距离
def Manhattan(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    return np.abs(npvec1-npvec2).sum()
# Chebyshev_Distance,切比雪夫距离
def Chebyshev(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    return max(np.abs(npvec1-npvec2))

# MahalanobisDistance,马氏距离
def Mahalanobis(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    npvec = np.array([npvec1, npvec2])
    sub = npvec.T[0]-npvec.T[1]
    inv_sub = np.linalg.inv(np.cov(npvec1, npvec2))
    return math.sqrt(np.dot(inv_sub, sub).dot(sub.T))
 '''
def show_distance(exit_point, c):
    line_point = np.array([exit_point, c])
    x = (line_point.T)[0]
    y = (line_point.T)[1]
    o_dis = round(Euclidean(exit_point, c), 2)  # 计算距离,更改函数名称
    mi_x, mi_y = (exit_point+c)/2  # 计算中点位置，来显示“distance=xx”这个标签
    plt.annotate('distance=%s' % str(o_dis), xy=(mi_x, mi_y), xycoords='data', xytext=(+10, 0), textcoords='offset points', fontsize=10, arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=.2"))
    return plt.plot(x, y, linestyle="--", color='black', lw=1)

show_distance(a1, c)
show_distance(a2, c)
show_distance(b1, c)
show_distance(b2, c)

plt.show()