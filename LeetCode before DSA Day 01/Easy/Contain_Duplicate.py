class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates = set()
        for i in nums:
            if i in duplicates:
                return True
            duplicates.add(i)
        return False
nums = [1,2,3,1]
S1 = Solution()
print(S1.containsDuplicate(nums))