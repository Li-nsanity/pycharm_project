import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
rv = st.poisson(2)
num_years = [4, 10, 7, 5, 4, 0, 0, 1]
x = range(8)
plt.bar(np.array(x)-.4, num_years, label='Observed instances')
plt.plot(x, sum(num_years)*rv.pmf(x), ls='dashed', lw =2, c='r', label='Poisson distribution\n$(\lambda=2.0)$')
plt.xlim([-1, 8])
plt.ylim([0, 11])
plt.xlabel('# of mass shootings in a year')
plt.ylabel('# of years')
plt.legend(loc='best')
plt.show()