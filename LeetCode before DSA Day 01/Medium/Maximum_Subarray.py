class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_num = max_global = nums[0]
        for i in nums[1:]:
            max_num = max(i, max_num + i)
            max_global = max(max_num, max_global)
        return max_global
nums = [-2,1,-3,4,-1,2,1,-5,4]
S1 = Solution()
print(S1.maxSubArray(nums))