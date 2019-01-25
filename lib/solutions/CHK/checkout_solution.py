from collections import Counter

PRICES = {"A": {1: 50, 3: 130, 5: 200},
          "B": {1: 30, 2: 45},
          "C": {1: 20},
          "D": {1: 15},
          "E": {1: }}

# e.g. 2 Es allow for the removal of 1 B.
REMOVERS = {"E": {2: ("B", 1)}}

PRICE_QUANTITIES = {product: sorted(deals.keys(), reverse=True) for product, deals in PRICES.iteritems()}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, basestring):
        return -1

    total = 0

    # First get the quantity of each product
    counts = Counter(skus)

    # Firstly, check the quantity removers (E)
    for product in REMOVERS:
        if product in counts:
            for









    # Loop through each product.
    # If it doesn't exist, return -1
    # If it does exist,
    #    loop through the quantities it is priced for from
    #    highest to lowest. If there is enough quantity,
    #    add the price to sum and remove quantity. Start again.

    # CHange this to use module so that I dont need a break and just one loop.
    for product, quantity in counts.iteritems():
        if product in PRICES:
            while quantity > 0:
                #print("quantity", product, quantity)
                for price_quantity in PRICE_QUANTITIES[product]:
                    #print("price quantity", product, price_quantity)
                    if price_quantity <= quantity:
                        quantity -= price_quantity
                        total += PRICES[product][price_quantity]
                        break
        else:
            return -1

    return total

print(checkout("AAAAAA"))
print(checkout("BBBB"))

