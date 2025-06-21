def DuplicateElement(arr):
    a = {}
    duplicates = []
    for i in arr:
        if i in a:
            duplicates.append(i)
        else:
            a[i] = 1
    return (list(set(duplicates)))
arr = [1, 2, 3, 4, 1, 2]
print(DuplicateElement(arr))
