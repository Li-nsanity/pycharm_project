from scipy.stats import poisson
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

t = 100
y = 0
m = 0
while True:
    x = np.random.exponential(2.0, 1)
    y = y + x
    m += 1
    if y > 100:
        break
    print(y, m)
