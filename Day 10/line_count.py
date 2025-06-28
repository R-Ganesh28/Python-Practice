
#readlines and count them
with open("demo.txt", "w")as file:
    file.write("Line1\n Line2\n Line3\nLine4")
with open("demo.txt", "r") as f:
    content = f.readlines()
    print("count =", len(content))

