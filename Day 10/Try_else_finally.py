# Show how all four blocks behave

try:
    y = int(input('Enter a number:'))
    x = y/0
except ZeroDivisionError:
    print("something went wrong zero Division Error!")
except ValueError:
    print("Its value error")
else:
    print(x)
finally:
    print("Sure.")
