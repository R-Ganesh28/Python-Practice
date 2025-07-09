class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
strs = ["flower","flow","flight"]
Sol = Solution()
print(Sol.longestCommonPrefix(strs))