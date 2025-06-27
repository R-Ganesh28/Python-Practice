#use zip()
def myfunc6(names, scores):
    x = dict(zip(names, scores))
    print(x)
names = ["Ganesh", "Sriram"]
scores = [90, 95]
myfunc6(names, scores)

#use enumerate()
def myfunc7(fruits):
    for index, values in enumerate(fruits):
        print(f"Index: {index}, key: {values}")
fruits = ["apple", "banana", "cherry"]
myfunc7(fruits)