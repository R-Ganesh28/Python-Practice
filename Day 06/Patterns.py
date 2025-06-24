#Right-angled Triangle
def rightangle():
    for i in range(6):
        print("*"*i)
rightangle()

print("--------------")
print(" ")
#Invert the Triangle
def invertangle():
    for i in range(5,-1, -1):
        print("*"*i)
invertangle()

print("----------------")
print(" ")
#Number pattern 
def Numbertriangle():
    for i in range(1, 6):
        for j in range(i):
            print(i, end=" ")
        print(" ")
Numbertriangle()
