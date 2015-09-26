import sys
import itertools


if __name__ == "__main__":
    for i in itertools.permutations(sys.argv[1]):
        print(''.join(i))
