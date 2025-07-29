import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        nums = math.sqrt(num)
        if nums == int(nums):
            return True
        else:
            return False
num = 16
sol = Solution()
print(sol.isPerfectSquare(num))