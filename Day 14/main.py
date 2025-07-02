import math
import datetime
import mymodule
from mypackage.calc import multiply, divide

#Built-in module
print("SquareRoot= ",math.sqrt(25))
print("Date AND Time= ", datetime.datetime.now())

#user-defined module
print("Addition:", mymodule.add(5,4))
print("Subtraction:", mymodule.sub(10,4))

#Package module
print("Multiplication: ", multiply(5,4))
print("Division:", divide(24,2))
