import sys
import numpy as np

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = np.loadtxt(filename, delimiter=',')
        for row_mean in np.mean(data, axis=1):
            print(row_mean)

if __name__ == '__main__':
    main()
