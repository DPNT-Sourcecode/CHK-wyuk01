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

    sum = 0

    counts = Counter(skus)
    print(counts)

    for product in counts:
        if product in counts:
            pass

        else:
            return -1

print(checkout(1))
print(checkout("ABCDEFAB"))





