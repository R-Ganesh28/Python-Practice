class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for i in s + t:
            result ^= ord(i)
        return chr(result)
s = "abcd"
t = "abcde"
S1 = Solution()
print(S1.findTheDifference(s,t))