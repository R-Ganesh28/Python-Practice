
# Handle both ValueError and ZeroDivisionError

try :
    y = int(input("Enter a number: "))
    x = y//0
except ZeroDivisionError:
    print("Zero Division Error")
        
except ValueError:
    print("Value Error")