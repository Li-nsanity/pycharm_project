import numpy as np
import pandas as pd

data1 = np.array([0.2, 0.2, 0.3, 0.3])
data2 = np.array([[0.7, 0.1, 0.1, 0.1],
                  [0.1, 0.6, 0.2, 0.1],
                  [0.1, 0.1, 0.6, 0.2],
                  [0.1, 0.1, 0.6, 0.2]])
sum = np.matmul(data1, data2)
sum1 = np.matmul(sum, data2)
print(sum1)
