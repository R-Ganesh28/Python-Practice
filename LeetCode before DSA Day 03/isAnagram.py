from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = list(s)
        T = list(t)
        return (Counter(S) == Counter(T))

S1 = Solution()
print(S1.isAnagram("anagram", "nagaram"))