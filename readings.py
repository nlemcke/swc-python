import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
            'Action is not one of --min, --mean, or --max: ' + action
    for filename in filenames:
        process(filename, action)

def process(filename, action):
    data = np.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = np.min(data, axis=1)
    elif action == '--mean':
        values = np.mean(data, axis=1)
    elif action == '--max':
        values = np.max(data, axis=1)

    for val in values:
        print(val)

if __name__ == '__main__':
    main()
