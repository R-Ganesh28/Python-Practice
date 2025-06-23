#Selection Sort
def Selection_Sort(mylist):
    n = len(mylist)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if mylist[j] < mylist[min_index]:
                min_index = j
        mylist[i], mylist[min_index] = mylist[min_index], mylist[i]    
    print("After:", mylist)
mylist = [7, 12, 9, 11, 3]
print('Before:', mylist)
Selection_Sort(mylist)