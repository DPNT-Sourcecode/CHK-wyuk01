from collections import Counter

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
          "K": {1: 80, 2: 150},
          "L": {1: 90},
          "M": {1: 15},
          "N": {1: 40},
          "O": {1: 10},
          "P": {1: 50, 5: 200},
          "Q": {1: 30, 3: 80},
          "R": {1: 50},
          "S": {1: 30},
          "T": {1: 20},
          "U": {1: 40},
          "V": {1: 50, 2: 90, 3: 130},
          "W": {1: 20},
          "X": {1: 90},
          "Y": {1: 10},
          "Z": {1: 50}}

# e.g. 2 Es allow for the removal of 1 B.
REMOVERS = {"E": (2, "B", 1),
            "F": (3, "F", 1),
            "N": (3, "M", 1),
            "R": (3, "Q", 1),
            "U": (4, "U", 1)}

PRICE_QUANTITIES = {product: sorted(deals.keys(), reverse=True) for product, deals in PRICES.iteritems()}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, basestring):
        return -1

    total = 0

    # First get the quantity of each product
    counts = Counter(skus)

    # Removals first
    for product, (num_needed_to_remove, product_to_remove, num_to_remove) in REMOVERS.iteritems():
        removal_instances = counts.get(product, 0) // num_needed_to_remove
        #print("instances", removal_instances)

        if product_to_remove in counts:
            new_count = max(0, counts[product_to_remove] - (num_to_remove * removal_instances))
            #print(counts[product_to_remove], new_count)
            counts[product_to_remove] = new_count

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