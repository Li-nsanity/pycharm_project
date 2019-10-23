from matplotlib import pyplot as plt
import random
import matplotlib

font = {'family': "Microsoft Yahei", 'size': '10'}
matplotlib.rc('font', **font)

plt.figure(figsize=(20, 8))
x = range(120)
y = [random.uniform(20, 35) for i in range(120)]

plt.plot(x, y, color='b', linestyle='-', linewidth='3')
_x_ticks = ["10点{}分".format(i) for i in range(60)]
_x_ticks += ["11点{}分".format(i - 60) for i in range(60, 120)]
plt.xticks(list(x)[::5], _x_ticks[::5], rotation=45)
plt.xlabel("时间")
plt.ylabel("温度 单位（C）")
plt.title("10点到12点温度变化情况")
# plt.savefig("./折线图1.svg")
plt.show()
