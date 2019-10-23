from matplotlib import pyplot as plt
import matplotlib

font = {'family': "Microsoft Yahei", 'size': '10'}
matplotlib.rc('font', **font)

plt.figure(figsize=(20, 8), dpi=80)
x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
plt.plot(x, y)
_x_ticks = ["{}岁".format(i) for i in range(11, 31)]
plt.xticks(x, _x_ticks)
plt.yticks(range(min(y), max(y) + 1))
plt.xlabel("年龄")
plt.ylabel("女朋友个数")
plt.title("统计年龄与女朋友个数的关系")
plt.grid(alpha=0.8)  # 绘制网格
plt.show()
