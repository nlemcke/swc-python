import numpy as np
data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
maxval, minval, stdval = np.max(data), np.min(data), np.std(data)
print('maximum:', maxval)
print('minimum:', minval)
print('standard deviation:', stdval)
print('avg daily inf:')
print(np.mean(data, axis=0))
