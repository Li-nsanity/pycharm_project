from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
df = pd.read_csv('./iris.csv', index_col=0)
df_shape = df.shape
df_train = df[["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]]
df_target = df["Species"]
train_X, test_X, train_Y, test_Y = train_test_split(df_train, df_target, test_size=0.2, random_state=0)
# random_state：设置随机种子的，为了每次迭代都有相同的训练集顺序
trainX_shape = train_X.shape
# x, y = df[:, :-1], df[:, -1]
# print(df)
print(trainX_shape)
print(train_X)

