from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float("inf")
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len
target = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(target, nums))