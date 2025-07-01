#Validate Email Format
import re
txt = "abdeviller@gmail.com"
x = bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', txt))
print(x)