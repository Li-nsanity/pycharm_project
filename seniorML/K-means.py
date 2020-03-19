import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
from sklearn import metrics
# X为样本特征，Y为样本簇类别，共1000个样本，每个样本2个特征，对应x和y轴，共4个簇，
# 簇中心在[-1,-1], [0,0],[1,1], [2,2]， 簇方差分别为[0.4, 0.2, 0.2]
X, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                  cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=9)
# plt.scatter(X[:, 0], X[:, 1], marker='o')  # 假设暂不知道y类别，不设置c=y，使用kmeans聚类
# plt.show()
# 不像监督学习的分类问题和回归问题，我们的无监督聚类没有样本输出，也就没有比较直接的聚类评估方法。
# 但是我们可以从簇内的稠密程度和簇间的离散程度来评估聚类的效果。
# 常见的方法有轮廓系数Silhouette Coefficient和Calinski-Harabasz Index。
# 个人比较喜欢Calinski-Harabasz Index，这个计算简单直接，得到的Calinski-Harabasz分数值s越大则聚类效果越好。
y_pred = KMeans(n_clusters=5, random_state=9).fit_predict(X)
print(metrics.calinski_harabasz_score(X, y_pred))
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
