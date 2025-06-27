#Nested Function
def myfunc5(n):
    return lambda i : i * n
multiplier = myfunc5(3)
print(multiplier(11))
