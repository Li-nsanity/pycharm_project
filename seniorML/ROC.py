# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:27:53 2020
演示目的：利用鸢尾花数据集画出ROC曲线,多分类
@author: Administrator
"""

# -*- coding: utf-8 -*-
print(__doc__)
 
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize   #二制化处理
from sklearn.multiclass import OneVsRestClassifier #一对其余模式
from scipy import interp

# 导入鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # X.shape==(150, 4)
y = iris.target  # y.shape==(150, )

# 二进制化输出
y = label_binarize(y, classes=[0, 1, 2])  # shape==(150, 3)
n_classes = y.shape[1]  # n_classes==3

# 添加噪音特征，使问题更困难 ，对X维度增加800维 150行 804列
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape  # n_samples==150, n_features==4
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]  # shape==(150, 84)

# 打乱数据集并切分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5,
                                                    random_state=0)
# X_train.shape==(75, 804), X_test.shape==(75, 804), y_train.shape==(75, 3), y_test.shape==(75, 3)

# 学习区分某个类与其他的类 调用一对其余模式转化为二类的分类问题
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,
                                 random_state=random_state))
y_score = classifier.fit(X_train, y_train).decision_function(X_test)
# y_score.shape==(75, 3)  预测分数，后面与真实值比较

# 为每个类别计算ROC曲线和AUC 计算性能评价结果
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):  #n_classes=3 所有行都要，第i列
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])
# fpr[0].shape==tpr[0].shape==(21, ), fpr[1].shape==tpr[1].shape==(35, ), fpr[2].shape==tpr[2].shape==(33, ) 
# roc_auc {0: 0.9118165784832452, 1: 0.6029629629629629, 2: 0.7859477124183007}

plt.figure()

# 计算微平均ROC曲线和AUC   ravel将多维数组降为一维
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

# 计算宏平均ROC曲线和AUC

# 首先汇总所有FPR
all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

# 然后再用这些点对ROC曲线进行插值
mean_tpr = np.zeros_like(all_fpr)
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])

# 最后求平均并计算AUC
mean_tpr /= n_classes

fpr["macro"] = all_fpr
tpr["macro"] = mean_tpr
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

# 绘制所有ROC曲线
plt.figure()
lw = 2
plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["micro"]),
         color='deeppink', linestyle=':', linewidth=4)

plt.plot(fpr["macro"], tpr["macro"],
         label='macro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["macro"]),
         color='navy', linestyle=':', linewidth=4)

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()

