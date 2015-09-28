import random

with open('/usr/share/dict/words') as wordsFile:
    dictionary = wordsFile.read().split('\n')

if __name__ == '__main__':
    print('95% "Guaranteed" Accurate Definition: ' + input(random.choice(dictionary) + ': '))
    # you know the definition already :)
