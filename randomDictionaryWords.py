import sys
import random

with open('/usr/share/dict/words') as wordsFile:
    dictionary = wordsFile.read().split('\n')

if __name__ == '__main__':
    # Prints a string that has the first word capitalized
    # and a . at the end, and it comes from a generator which chooses
    # a random word from a dictionary for the int supplied to the script
    print((' '.join([random.choice(dictionary) for i in range(int(sys.argv[1]))]) + ".").capitalize())
