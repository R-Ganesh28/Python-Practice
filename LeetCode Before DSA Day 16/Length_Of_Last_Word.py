class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

s = "luffy is still joyboy"
sol = Solution()
print(sol.lengthOfLastWord(s))