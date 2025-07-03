class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in arr:
                return (arr[complement], i)
            arr[num] = i
nums = [2,7,11,15]
target = 9
S1 = Solution()
print(S1.twoSum(nums, target))