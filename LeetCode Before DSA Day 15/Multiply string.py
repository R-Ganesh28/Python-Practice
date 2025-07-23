class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        return str(num1*num2)
num1 = "123"
num2 = "456"
sol = Solution()
print(sol.multiply(num1, num2))