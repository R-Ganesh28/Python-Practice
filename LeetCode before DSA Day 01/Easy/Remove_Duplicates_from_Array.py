class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l = l + 1
        return l
nums = [0,0,1,1,1,2,2,3,3,4]
S1 = Solution()
print(S1.removeDuplicates(nums))