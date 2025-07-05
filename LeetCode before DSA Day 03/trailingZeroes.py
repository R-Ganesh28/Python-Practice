class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
n = 5    
S1 = Solution()
print(S1.trailingZeroes(n))