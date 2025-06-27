#List Comprehension
def myfunc3():
    return list(i*i for i in range(1, 11))
print(myfunc3())

#Dictionary Comprehension
def myfunc4():
    x = {i : i ** 2 for i in range(1, 6)}
    print(x)
myfunc4()

