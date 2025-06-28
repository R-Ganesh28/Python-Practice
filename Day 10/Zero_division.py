
# Divide two numbers and handle ZeroDivisionError
def myfunc():
    try :
        x = 10/0
        print(x)
    except ZeroDivisionError:
        print("Zero Division Error")
myfunc()