import math
import random

def slowfun(x, y, cache={}):
    # TODO: Modify to produce the same results, but much faster
    if (x, y) not in cache:
        cache[(x, y)] = math.pow(x, y)
        cache[(x, y)] = math.factorial(cache[(x, y)])
        cache[(x, y)] //= (x + y)
        cache[(x, y)] %= 982451653

    return cache[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
