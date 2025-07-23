class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
x = 2.000001
n = 10
sol = Solution()
print(sol.myPow(x,n))