import random
import sys


# based on random's shuffle
def ig_shuffle(x):
    # [brian] Nice! A fisher-yates shuffle, this is a great algorithm to know.
    for i in reversed(range(1, len(x))):
        j = random.randrange(0, i+1)
        x[i], x[j] = x[j], x[i]
    return x


# This will print the arguments in a random order
if __name__ == '__main__':
    print(ig_shuffle(sys.argv[1:]))
