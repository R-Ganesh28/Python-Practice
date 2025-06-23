#Insertion Sort
def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1
    print("After:", arr)
arr = [7, 12, 9, 11, 3]
print("Before:", arr)
Insertion_Sort(arr)