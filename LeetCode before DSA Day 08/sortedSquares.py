class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        pos = n - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return result
nums = [-7,-3,2,3,11]
Sol = Solution()
print(Sol.sortedSquares(nums))