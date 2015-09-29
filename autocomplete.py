import sys
import re

with open('/usr/share/dict/words') as wordsFile:
    dictionary = wordsFile.read().split('\n')

if __name__ == "__main__":
    search = re.compile(sys.argv[1] + '[A-z]*', re.IGNORECASE)
    for word in dictionary:
        if search.match(word):
            print(word)
