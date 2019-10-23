import numpy as np




# 创建数据集的biaoqian
def createDataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']

    return group, labels

dataset,labels= createDataset()
# KNN算法实验版。vecX为待分类向量，dataset为已知标签数据集，label为标签，K为距离最小的K个值
def KNN_classify0(vecX, dataset, label, k):
    datasetsize = dataset.shape[0]  # 获取数据集的大小
    # 欧式距离
    diffmat = np.tile(vecX, (datasetsize, 1)) # tile() 建立维度与dataset相等的数组 大小与dataset相等,内容均为vecx
    distances = np.sum(np.power(diffmat-dataset, 2), axis=1)**0.5
    sortdistances = distances.argsort()  # 返回排序后的索引
    # 选择距离最小的K个点
    suma = 0
    sumb = 0
    for i in range(k):
        if label[sortdistances[i]] == 'A':
            suma += 1
        if label[sortdistances[i]] == 'B':
            sumb += 1
    return 'A'  if suma > sumb else 'B'



if __name__ == '__main__':
    print(KNN_classify0([0.2, 0.15], dataset, labels, 3))