from collections import Counter

PRICES = {"A": {1: 50, 3: 130},
          "B": {1: 30, 2: 45},
          "C": {1: 20},
          "D": {1: 15}}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, basestring):
        return -1

    sum = 0

    # First get the quantity of each product
    counts = Counter(skus)
    print(counts)

    # Loop through each product.
    # If it doesn't exist, return -1
    # If it does exist,
    #    loop through the quantities it is priced for from
    #    highest to lowest. If there is enough quantity,
    #    add the price to sum and remove quantity. Start again.
    for product, quantity in counts.iteritems():
        if product in PRICES:
            price_quantities = sorted(PRICES[product].keys(), reverse=True)

            while quantity > 0:
                for price_quantity in price_quantities:
                    if price_quantity <= quantity:
                        quantity -= price_quantity
                        sum += PRICES[product][price_quantity]
        else:
            return -1

    return sum


print(checkout(1))
print(checkout("ABABB"))









