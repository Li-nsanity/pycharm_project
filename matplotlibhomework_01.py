from matplotlib import pyplot as plt
import matplotlib
import numpy as np

font = {'family': "Microsoft Yahei", 'size': '10'}
matplotlib.rc('font', **font)

plt.figure(figsize=(20, 8), dpi=80)
x = range(11, 31)
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
plt.plot(x, y1, label="自己", color="orange", linestyle=":")
plt.plot(x, y2, label="同桌", color="cyan", linestyle="-.")
_x_ticks = ["{}岁".format(i) for i in range(11, 31)]
plt.xticks(x, _x_ticks)
plt.yticks(range(0, 9))
plt.xlabel("年龄")
plt.ylabel("女朋友个数")
plt.title("统计年龄与女朋友个数的关系")
plt.grid(alpha=0.8)  # 绘制网格
plt.legend(loc="upper right")  # 添加图例
plt.text(x=25,  # 水印开头左下角对应的X点
         y=5,  # 水印开头左下角对应的Y点
         s="Li-nsanity",  # 水印文本
         fontsize=50,  # 水印大小
         color="orange",  # 水印颜色
         alpha=0.5)
for xy in zip(x, y1):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')
for xy in zip(x, y2):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')

plt.show()
