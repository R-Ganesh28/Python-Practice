#Linear Search
def LinearSearch(arr, goal):
    for i in range(len(arr)):
        if arr[i] == goal:
            return i
    return -1

arr = [3, 6, 9, 7, 12, 15]
goal = 6
result = LinearSearch(arr, goal)
if result == -1:
    print("Not Found.")
else:
    print(f"Found in index {result}")
