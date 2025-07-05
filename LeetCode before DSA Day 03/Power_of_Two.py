import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
n = 16    
S1 = Solution()
print(S1.isPowerOfTwo(n))