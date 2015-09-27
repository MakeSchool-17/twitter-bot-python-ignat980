import sys
import random

dictionary = open('/usr/share/dict/words').read().split('\n')

if __name__ == '__main__':
    print((' '.join([random.choice(dictionary) for i in range(int(sys.argv[1]))]) + ".").capitalize())
