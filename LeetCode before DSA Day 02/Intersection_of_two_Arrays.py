class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
nums1 = [1,2,2,1]
nums2 = [2,2]
S1 = Solution()
print(S1.intersection(nums1,nums2))