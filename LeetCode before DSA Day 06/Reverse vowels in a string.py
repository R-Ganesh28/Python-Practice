class Solution:
    def modify(self, s):
        output = set('aeiouAEIOU')
        s = list(s)
        i , j = 0, len(s)-1
        while i < j:
            if s[i] not in output:
                i += 1
            elif s[j] not in output:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)

sol = Solution()
print(sol.modify("practice"))