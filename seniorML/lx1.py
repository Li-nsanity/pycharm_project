import numpy as np

from scipy.stats import pearsonr

x = np.random.uniform(-1, 1, 100000)

print (pearsonr(x, x*2)[0] )

print (pearsonr(x, x**2)[0] )


