from collections import Counter

PRICES = {"A": {1: 50, 3: 130, 5: 200},
          "B": {1: 30, 2: 45},
          "C": {1: 20},
          "D": {1: 15},
          "E": {1: 40},
          "F": {1: 10}}

# e.g. 2 Es allow for the removal of 1 B.
REMOVERS = {"E": (2, "B", 1),
            "F": (3, "F", 1)}

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