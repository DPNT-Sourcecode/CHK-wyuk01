from collections import Counter

PRICES = {"A": {1: 50, 3: 130},
          "B": {1: 30, 2: 45},
          "C": {1: 20},
          "D": {1: 15}}

PRICE_QUANTITIES = {product: sorted(deals.keys(), reverse=True) for product, deals in PRICES.iteritems()}

print(PRICE_QUANTITIES)

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, basestring):
        return -1

    total = 0

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
            while quantity > 0:
                for price_quantity in PRICE_QUANTITIES[product]:
                    print("checking price quantity " + str(price_quantity))
                    print("quantity for " + product + " is " + str(quantity))
                    if price_quantity <= quantity:
                        quantity -= price_quantity
                        total += PRICES[product][price_quantity]
        else:
            return -1

    return total

checkout("AA")
