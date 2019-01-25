# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if type(x) is not int or type(y) is not int:
        raise TypeError("x and y should be integers between 0 and 100")

    if x < 0 or x > 100 or y < 0 or y > 100:
        raise ValueError("x and y should be between 0 and 100")

    return x + y;

