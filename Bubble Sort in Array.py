#Bubble Sort
def Bubble_Sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    print("After:", arr)
arr = [7, 12, 9, 11, 3]
print("Before:", arr)
Bubble_Sort(arr)