from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        sorted_items = sorted(freq.items(), key = lambda item: item[1], reverse = True)
        result = [item[0] for item in sorted_items [:k]]
        return result
nums = [1,1,1,2,2,3]
k = 2
S1 = Solution()
print(S1.topKFrequent(nums, k))