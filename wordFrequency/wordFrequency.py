import re
import collections


h = collections.Counter()
regxWordsPattern = re.compile('[A-Za-z\']+')


def histogramFromFile(filename):
    with open(filename) as corpus:
        return histogramFromString(corpus.read())


def histogramFromString(source):
    words = re.findall(regxWordsPattern, source.lower())
    for word in words:
        h[word] += 1
    return h


def unique_words(hg):
    return 'There are ' + str(len(hg)) + ' unique words.'


def frequency(word, hg):
    if hg[word]:
        return '"' + str(word).capitalize() + '"\
 occurs ' + str(hg[word]) + ' times.'
    else:
        return 'Word not found.'


if __name__ == '__main__':
    if str(input('Input from a "file" or "string": ')).startswith('f'):
        try:
            print(histogramFromFile(input('File name: ')).most_common())
        except:
            print('File not found.')
            exit()
    else:
        print(histogramFromString(input('String: ')).most_common())
    func = input('What do you want to do? (u for total unique words,'
                 ' f for number of times a word appears in the text,'
                 ' q for quit): ')
    while func != 'q':
        if func == 'u':
            print(unique_words(h))
        elif func == 'f':
            print(frequency(input('Word for frequency: ').lower(), h))
        func = input('What do you want to do? (u for total unique words,'
                     ' f for number of times a word appears in the text,'
                     ' q for quit): ')
    else:
        exit()
