import sys
import random

with open('/usr/share/dict/words') as words:
    dictionary = words.read().split('\n')

if __name__ == '__main__':
    print((' '.join([random.choice(dictionary) for i in range(int(sys.argv[1]))]) + ".").capitalize())
