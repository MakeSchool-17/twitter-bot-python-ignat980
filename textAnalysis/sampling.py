import random
import wordFrequency
import sys


class WeightedRandomizer:
    def __init__(self, weights):
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
                wr = WeightedRandomizer(wordFrequency.histogramFromFile(
                    input('File name: ')))
            else:
                wr = WeightedRandomizer(wordFrequency.histogramFromFile(
                    sys.argv[1]))
        except:
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
