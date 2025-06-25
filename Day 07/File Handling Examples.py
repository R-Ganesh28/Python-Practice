with open("sample.txt", 'w') as f:
    f.write("Hi This is a sample file.")
    
with open("sample.txt", 'r') as f:
    print(f.read())

with open("sample.txt", 'a') as file:
    file.write("\nHello a python programming.")

with open("sample.txt", 'r') as f:
    content = f.readline()
    print(content)
    print(f.readline())
