#Factorial
def Factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return (N * Factorial(N-1))
print(Factorial(5))

print("---------------------")
#Fibonnaci Series
def Fibonnaci(N):
    if N <= 1:
        return N
    else:
        return (Fibonnaci(N-1)+Fibonnaci(N-2))

print(Fibonnaci(6))

print("---------------------")
#Sum of Array using Recursion
def sumarray(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sumarray(arr[1:])
arr = [1, 2, 3, 4, 5, 6]
print(sumarray(arr))

print("---------------------")
#Sum of digit using Recursion
def sumdigit(n):
    if n == 0:
        return n
    else:
        return n % 10 + sumdigit(n//10)
n = 123
print(sumdigit(n))

print("--------------------")

#Palindrome using Recursion
def palindrome(an):
    if len(an) <= 1:
        return True
    else:
        if an[0] == an[-1]:
            return palindrome(an[1:-1])
        else:
            return False
an = "madaM"
print(palindrome(an.lower()))