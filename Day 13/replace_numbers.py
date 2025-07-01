#Replace numbers with hyphen
import re
txt = "The9rain9in9Spain"
x = re.sub('[0-9]', '_', txt)
print(x)