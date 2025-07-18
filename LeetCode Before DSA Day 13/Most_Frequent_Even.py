from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        evens = [num for num in nums if num % 2 == 0]
        if not evens:
            return -1
        freq = Counter(evens)
        max_freq = max(freq.values())

        return min(num for num in freq if freq[num] == max_freq)
    
nums = [0,1,2,2,4,4,1]
sol = Solution()
print(sol.mostFrequentEven(nums))