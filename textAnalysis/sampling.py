import random
import wordFrequency
import sys


# [brian] Neat! A nice approach
class WeightedRandomizer(object):
    def __init__(self, weights):
        # [brian] Using double-underscores is usually a bad idea in python. It
        # makes things private but there's a saying, "we are all consenting adults here".
        # You shouldn't make things private unless you have to. These should probably be
        # called `self._max` and `self._weights`.
        self.__max = .0
        self.__weights = []
        for value, weight in weights.items():
            self.add(weight, value)

    def add(self, weight, value):
        self.__max += weight
        self.__weights.append((self.__max, value))

    def random(self):
        r = random.random() * self.__max
        for ceil, value in self.__weights:
            if ceil > r:
                return value


if __name__ == '__main__':
    if str(sys.argv[1]).endswith('.txt'):
        try:
            if len(sys.argv) == 1:
                # [brian] I don't think this will ever be hit. You'll get an IndexError before it does!
                wr = WeightedRandomizer(wordFrequency.histogramFromFile(
                    input('File name: ')))
            else:
                wr = WeightedRandomizer(wordFrequency.histogramFromFile(
                    sys.argv[1]))
        except: # [brian] This should be `except FileNotFoundError` (or IOError if you use python 2)
            # catching every exception is a really, really, bad idea. What if you have a bug in your code,
            # and an exception which isn't related to files is thrown? Your program will lie to you! And
            # make things harder to debug.
            print('File not found.')
            exit()
    else:
        wr = WeightedRandomizer(wordFrequency.histogramFromString(
            input('String: ')))
    if len(sys.argv) == 3 and str(sys.argv[2]).isdigit:
            more = int(sys.argv[2])
    else:
        more = int(input('Generate how many words? '))
    wordFrequency.h.clear()
    if more != 0:
        for i in range(0, more):
            wordFrequency.h[wr.random()] += 1
        print(wordFrequency.h.most_common())
