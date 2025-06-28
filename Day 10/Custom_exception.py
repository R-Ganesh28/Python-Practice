    
# Raise an exception if age is less than 18
class UnderageError(Exception):
    pass
age = int(input("Enter a number: "))
if age < 18:
    raise UnderageError("You need to be atleast 18 year old")
else:
    print("Access Granted.")
