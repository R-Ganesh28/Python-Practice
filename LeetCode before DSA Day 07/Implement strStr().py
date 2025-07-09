class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

haystack = "sadbutsad"
needle = "sad"
s = Solution()
print(s.strStr(haystack, needle))