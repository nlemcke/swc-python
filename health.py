import numpy as np
import matplotlib.pyplot as plt
import glob

def visualize(filename):

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0), drawstyle='steps-mid')

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0), drawstyle='steps-mid')

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0), drawstyle='steps-mid')

    fig.tight_layout()

    plt.show()

def finderrors(filename):

    data = np.loadtxt(fname=filename, delimiter=',')
    max_d0 = np.max(data, axis=0)[0]
    max_d20 = np.max(data, axis=0)[20]

    if max_d0 == 0 and max_d20 == 20:
        print('Suspicious looking maxima!')
    elif np.sum(np.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')

# visualize('data\inflammation-01.csv')
finderrors('data\inflammation-01.csv')
