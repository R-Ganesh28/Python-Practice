import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        return str(int(num1) + int(num2))
    
num1 = "456"
num2 = "77"
sol = Solution()
print(sol.addStrings(num1,num2))