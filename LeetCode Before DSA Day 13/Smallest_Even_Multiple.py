class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2
    
n = 6
sol = Solution()
print(sol.smallestEvenMultiple(n))