from matplotlib import pyplot as plt
import matplotlib

font = {'family': "Microsoft Yahei", 'size': '10'}
matplotlib.rc('font', **font)

plt.figure(figsize=(20, 8), dpi=80)
x_3 = range(0, 31)
x_10 = range(50, 81)
y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22,
       23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12,
        13, 6]
plt.scatter(x_3, y_3, label="三月")
plt.scatter(x_10, y_10, label="十月")
_x = list(x_3) + list(x_10)
_x_ticks = ["三月{}日".format(i) for i in x_3]
_x_ticks += ["十月{}日".format(i - 50) for i in x_10]
plt.xticks(_x[::3], _x_ticks[::3], rotation=45)
plt.legend(loc="upper right")  # 添加图例
plt.title("北京2016年3,10月份每天白天的最高气温")
plt.ylabel("3月，10月北京白天最高气温")
plt.show()
