
#filenot found error
try:
    with open("demo.txt", 'r')as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")