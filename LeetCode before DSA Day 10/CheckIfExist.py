class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for i in arr:
            if i*2 in seen or (i % 2 ==0 and i // 2 in seen):
                return True
            seen.add(i)
        return False
    
arr = [10,2,5,3]
sol = Solution()
print(sol.checkIfExist(arr))