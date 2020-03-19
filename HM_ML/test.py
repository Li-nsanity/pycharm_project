import numpy as np
import pandas as pd
data = pd.read_excel("./test.xls")
arr = np.array(data['日期'])
df =pd.DataFrame(data)
#  arr = arr.tostring()
arr2 = []
for i in arr:
    temp = str(int(i))
    arr2.append(temp[4:6])

data2 = np.array(arr2)
df['日期'] = data2
print(df)