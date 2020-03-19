from sklearn.model_selection import KFold
import pandas as pd
df = pd.read_csv('./iris.csv', index_col=0)
kf = KFold(n_splits=10, shuffle=False, random_state=None)
'''n_splits表示将数据分成几份；shuffle和random_state表示是否随机生成。
如果shuffle = False,random_state = None,重复运行将产生同样的结果；
如果shuffle = True,random_state = None,重复运行将产生不同的结果；
如果shuffle = True,random_state = （一个数值）,重复运行将产生相同的结果；
'''
for train, test in kf.split(df):
    print("%s %s" % (train, test))