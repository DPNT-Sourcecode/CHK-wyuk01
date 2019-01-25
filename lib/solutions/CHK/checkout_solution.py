from collections import Counter

PRICES = {"A": {1: 50, 3: 130},
          "B": {1: 30, 2: 35},
          "C": {1: 20},
          "D": {1: 15}}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, basestring):
        return -1

    counts = Counter(skus)

    print(counts)


checkout("ABCDEFAB")




