import sys
import re

with open('/usr/share/dict/words') as wordsFile:
    dictionary = wordsFile.read().split('\n')

if __name__ == "__main__":
    search = re.compile(sys.argv[1] + '[A-z]*', re.IGNORECASE)
    # [brian] To make this a little more readable, a python programmer would probably do:
    search = re.compile('{}[A-z]*'.format(sys.argv[1]), re.IGNORECASE)
    # it's longer, but `+` is used for so many different things that it takes a
    # second to figure out. ''.format() is obviously creating a string from
    # different components.
    for word in dictionary:
        if search.match(word):
            print(word)
