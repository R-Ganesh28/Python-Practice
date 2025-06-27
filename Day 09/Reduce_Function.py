#Lambda + reduce()
from functools import reduce
def myfunc2():
    return reduce(lambda x, y : x + y, numbers)
numbers = [1, 2, 3, 4, 5]
print(myfunc2())
