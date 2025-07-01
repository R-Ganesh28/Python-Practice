#Extract all words from string
import re 
txt = "The rain in Spain"
x = re.findall(r"\w+",txt)
print(x)