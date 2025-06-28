#write,read, append
with open("demo.txt", 'w')as f:
    f.write("This is used for write.")
with open("demo.txt", 'a') as f:
    f.write("Hello, This is program.")
with open("demo.txt", 'r')as f:
    content = f.read()
    print(content)
