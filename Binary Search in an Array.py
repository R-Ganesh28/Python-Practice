#Binary Search
def BinarySearch(array, search, low, high):
    while low <= high:
        middle = low + (high - low) // 2
        if search < array[middle]:
            high = middle - 1
        elif search > array[middle]:
            low = middle + 1
        else:
            return middle
    return -1
        
array = [1, 3, 5, 7, 9]
search = 9
low = 0
high = len(array) - 1
results = BinarySearch(array, search, low, high)
if results == -1:
    print("Not Found.")
else:
    print("Found in index", results)
