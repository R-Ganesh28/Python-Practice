import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        Rev = re.sub(r"[^a-zA-Z0-9]","",s.lower())
        return Rev == Rev[::-1]
s = "A man, a plan, a canal: Panama"
S1 = Solution()
print(S1.isPalindrome(s))