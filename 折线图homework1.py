# 如果列表a表示10点到12点的每一分钟的气温,如何绘制折线图观察每分钟气温的变化情况?
# a= [random.randint(20,35) for i in range(120)]
from matplotlib import pyplot as plt
import random

fig = plt.figure(figsize=(20, 8), dpi=80)
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.xticks(range(2, 121, 4))
plt.yticks(range(20, 35))

plt.plot(x, y)
plt.show()
