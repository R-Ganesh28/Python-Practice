# Check if string has digits
import re
txt = "Hello9"
x = bool(re.search(r"\d",txt))
print(x)
