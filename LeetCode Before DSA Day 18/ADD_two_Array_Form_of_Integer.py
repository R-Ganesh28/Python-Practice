class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        result = []
        i = len(num) - 1

        while i >= 0 or k>0:
            if i >= 0:
                k += num[i]
                i -= 1
            result.append(k % 10)
            k //= 10
        return result[::-1]

num = [2,1,5]
k = 806
sol = Solution()
print(sol.addToArrayForm(num, k))