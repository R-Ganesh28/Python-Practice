class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        i = 0
        i1 = 1
        for _ in range(2, n + 1):
            i, i1 = i1,i1+i
        return i1
S1 = Solution()
print(S1.fib(4))