from collections import Counter
from textwrap import wrap
import re

PRICES = {"A": {1: 50, 3: 130, 5: 200},
          "B": {1: 30, 2: 45},
          "C": {1: 20},
          "D": {1: 15},
          "E": {1: 40},
          "F": {1: 10},
          "G": {1: 20},
          "H": {1: 10, 5: 45, 10: 80},
          "I": {1: 35},
          "J": {1: 60},
          "K": {1: 70, 2: 120},
          "L": {1: 90},
          "M": {1: 15},
          "N": {1: 40},
          "O": {1: 10},
          "P": {1: 50, 5: 200},
          "Q": {1: 30, 3: 80},
          "R": {1: 50},
          "S": {1: 20},
          "T": {1: 20},
          "U": {1: 40},
          "V": {1: 50, 2: 90, 3: 130},
          "W": {1: 20},
          "X": {1: 17},
          "Y": {1: 20},
          "Z": {1: 21}}

PRICE_QUANTITIES = {product: sorted(deals.keys(), reverse=True) for product, deals in PRICES.iteritems()}

# e.g. 2 Es allow for the removal of 1 B.
REMOVERS = {"E": (2, "B", 1),
            "F": (3, "F", 1),
            "N": (3, "M", 1),
            "R": (3, "Q", 1),
            "U": (4, "U", 1)}

# products in the deal listed in descending order of price per unit
COMBO_DEAL = (frozenset(["S", "T", "X", "Y", "Z"]), 3, 45)

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, basestring):
        return -1

    total = 0

    # Get the quantity of each product
    counts = Counter(skus)

    # Firstly handle combo deals.
    # This is horrifically inefficient :(
    products, amount, price = COMBO_DEAL

    # make a regular expression:
    regex = "[^" + "".join(products) + "]"
    deal_skus = re.sub(regex, )

    # Split into multiples
    wrap(deal_skus, amount)









    # Secondly handle removals
    for product, (num_needed_to_remove, product_to_remove, num_to_remove) in REMOVERS.iteritems():
        removal_instances = counts.get(product, 0) // num_needed_to_remove

        if product_to_remove in counts:
            counts[product_to_remove] = new_count

    # Lastly handle standard multiple items

    # Loop through each product.
    # If it doesn't exist, return -1
    # If it does exist,
    #    loop through the quantities it is priced for from
    #    highest to lowest. If there is enough quantity,
    #    add the price to sum and remove quantity. Start again.
    for product, quantity in counts.iteritems():
        if product in PRICES:
            for price_quantity in PRICE_QUANTITIES[product]:
                saving_instances = quantity // price_quantity

                if saving_instances > 0:
                    total += PRICES[product][price_quantity] * saving_instances
                    quantity -= price_quantity * saving_instances

        else:
            return -1

    return total

#print(checkout("AAAAAA"))
#print(checkout("BBBBEEEE"))
#print(checkout("FFFF"))




