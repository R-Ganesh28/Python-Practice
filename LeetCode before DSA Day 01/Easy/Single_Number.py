class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result
nums = [2,2,1]
S1 = Solution()
print(S1.singleNumber(nums))