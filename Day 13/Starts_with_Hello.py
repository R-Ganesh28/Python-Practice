#Check if string starts with 'Hello'
import re
txt = "Hello The rain in Spain"
x = bool(re.match('^Hello', txt))
print(x)
