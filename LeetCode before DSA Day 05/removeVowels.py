def removeVowels(s):
    output = ""
    for i in s.lower():
        if i in 'aeiou':
            continue
        output += i
    return output

s = "welcome to geeksforgeeks"
print(removeVowels(s)) 
