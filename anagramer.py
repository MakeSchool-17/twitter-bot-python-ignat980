import sys
import enchant  # Uses PyEnchant for connecting to enchant


def anagrams(word):
    """ Generate all of the permutations of a word. """
    if len(word) < 2:  # A letter does not need to be permutated
        yield word
    else:
        for i, letter in enumerate(word):
            if letter not in word[:i]:  # Avoid duplicates
                for j in anagrams(word[:i]+word[i+1:]):  # Yay recursion
                    yield j+letter


if __name__ == "__main__":
    d = enchant.Dict('en_US')  # Initialize the dictionary
    for i in anagrams(sys.argv[1]):
        if d.check(i):
            print(i)
