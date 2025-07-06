
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        x = 1
        while x < n:
            x*= 3
        return n == x
n = 27
S1 = Solution()
print(S1.isPowerOfThree(n))