#Count Frequency of Each Element in a list using Dictionary
def CountFrequency(array):
    a = {}
    for i in array:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    print(a)
array = ["apple", "Cherry", "apple", "Cherry", "apple", "Banana"]
CountFrequency(array)