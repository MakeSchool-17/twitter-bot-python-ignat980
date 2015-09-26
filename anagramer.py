import sys
import itertools
import enchant


anagrams = []

if __name__ == "__main__":
    d = enchant.Dict('en_US')
    for i in range(2, len(sys.argv[1])):
        for word in itertools.permutations(sys.argv[1], i):
            r = ''.join(word)
            if d.check(r):
                if r not in anagrams:
                    anagrams.append(r)
                    print(r)
