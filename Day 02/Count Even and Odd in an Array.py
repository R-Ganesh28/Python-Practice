def countevnodd(even):
    count = 0
    count1 = 0
    for i in range(len(even)):
        if even[i]%2==0:
            count += 1
        else:
            count1 += 1
    print(f"Even = {count}, Odd = {count1}")
even = [1,2,3,4,5,7]
countevnodd(even)