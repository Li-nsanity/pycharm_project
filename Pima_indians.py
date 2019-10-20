# 先导入所有要用的Class
import numpy  # 数值计算工具
import pandas as pd  # 数据科学计算工具
import matplotlib.pyplot as plt  # 可视化
import seaborn as sns   # matplotlib的高级API
import xgboost
from sklearn import cross_decomposition
from sklearn.metrics import accuracy_score
# %matplotlib inline # 在Notebook里面作图/嵌图

# load数据集
dataset = numpy.loadtxt('.//Datasource//pima-indians-diabetes.data.csv', delimiter=",")

# pima = pd.read_csv('.//Datasource//pima-indians-diabetes.data.csv', delimiter=",")
# pima.head()
# pima.describe()
# 把 X Y 分开
X = dataset[:,0:8]
Y = dataset[:,8]

# 现在我们分开训练集和测试集
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = cross_validation.train_test_split \
(X, Y, test_size=test_size, random_state=seed)
# 训练模型
model = xgboost.XGBClassifier()
model.fit(X_train, y_train)
# 做预测
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# 显示准确率
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

# 更多的模型：
import sklearn.ensemble.RandomForestClassifier
import sklearn.ensemble.RandomForestRegressor
import sklearn.ensemble.AdaBoostClassifier
import sklearn.ensemble.AdaBosstRegressor