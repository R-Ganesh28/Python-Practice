#Reverse string
def reverse_string(s):
    return s[::-1]
s = "Hello"
print(reverse_string(s))

#Count Words
def countwords(s):
    return len(s.strip().split())
s = "Hello World"
print(countwords(s))

#Check if Anagram
def is_anagram(s, t):
    return sorted(s) == sorted(t)
s = "Silent"
t = "Listen"
print(is_anagram(s.lower(), t.lower()))

#Replace with Hyphen String
def hyphen_string(s):
    return s.replace(" ","-")
s = "This is a Python String Manipulation Program"
print(hyphen_string(s))
