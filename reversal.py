import sys


if __name__ == '__main__':
    if len(sys.argv[1:]) == 1:
        print(sys.argv[1][::-1])
    else:
        print(' '.join(sys.argv[1:][::-1]))
