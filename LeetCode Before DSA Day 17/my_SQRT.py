import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
x = 8
sol = Solution()
print(sol.mySqrt(x))