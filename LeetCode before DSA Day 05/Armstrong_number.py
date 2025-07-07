def Armstrong(N):
    Number = str(N)
    D = len(Number)
    output = 0
    for i in Number:
        output += int(i) ** D
    return output == N
N = 153
print(Armstrong(N))