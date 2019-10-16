from matplotlib import pyplot as plt
# 1.设置图片大小(想要一个高清无码大图)
# 2.保存到本地
# 3.描述信息,比如x轴和y轴表示什么,这个图表示什么
# 4.调整x或者y的刻度的间距
# 5.线条的样式(比如颜色,透明度等)
# 6.标记出特殊的点(比如告诉别人最高点和最低点在哪里)
# 7.给图片添加一个水印(防伪,防止盗用)
# ----------------------------------------------------

# 设置图片大小 figsize =(宽，高) dpi 每英寸上点的个数
fig = plt.figure(figsize=(20, 8), dpi= 80)
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 绘图  传入X,Y，通过plot绘图
plt.plot(x, y)

# 设置X轴的刻度 ::3取步长 0.5 ：：3 就是隔1.5一个刻度
_xticks_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xticks_labels[::3])
# plt.xticks(range(2, 24))

# 设置Y轴刻度
plt.yticks(range(min(y)-1, max(y)+1))

# 保存svg这种矢量图格式，放大之后不会有锯齿
# plt.savefig("./折线图.svg")

# 展示图形
plt.show()
