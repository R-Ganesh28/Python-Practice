#Lambda + Map
def myfunc(num):
    for i in num:
        return list(map(lambda i : i * 2, num))
num = [1, 2, 3, 4, 5]
print(myfunc(num))

#Lambda + Filter
def myfunc1(num):
    for i in num:
        return (list(filter(lambda i : i % 2 == 0, num)))
num = [10, 43, 51, 37, 22]
print(myfunc1(num))