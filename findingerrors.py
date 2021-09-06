import numpy as np
data = np.loadtxt('data\inflammation-01.csv', delimiter=',')
max_d0 = np.max(data, axis=0)[0]
max_d20 = np.max(data, axis=0)[20]

if max_d0 == 0 and max_d20 == 20:
    print('Suspicious looking maxima!')
elif np.sum(np.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')
