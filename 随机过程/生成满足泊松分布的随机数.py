import numpy as np
from tkinter import *

root = Tk(className='生成泊松分布随机数')
root.geometry("400x300")
# 输入lamda
label1 = Label(root)
label1['text'] = '请输入一个数学期望lamda:'
label1.grid(row=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)
# 输入k
label2 = Label(root)
label2['text'] = '请输入生成随机个数k:'
label2.grid(row=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1)


# 按钮绑定的动作
def print1():
    result = Tk(className="result")
    result.geometry("200x50")
    S1 = Scrollbar(result, orient=HORIZONTAL)
    S1.pack(side=BOTTOM, fill=X)
    if entry1.get() == '':
        lab = Label(result, text="请输入lamda!")
        lab.pack(side=LEFT)
    elif entry2.get() == '':
        lab2 = Label(result, text="请输入k!")
        lab2.pack(side=LEFT)
    else:
        x = int(entry1.get())
        k = int(entry2.get())
        if x > 0 and k > 0:
            x1 = np.random.poisson(lam=x, size=k)
            rst = Label(result, text=x1)
            rst.pack(side=LEFT)
        else:
            label3 = Label(result, text="输入内容有错，lamda请输入正整数,k请输入正整数")
            label3.pack(side=LEFT)


# 生成按钮
btn = Button(root, command=print1)
btn['text'] = '生成'
btn.grid(row=2)

# 进入消息循环
root.mainloop()
