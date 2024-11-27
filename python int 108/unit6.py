#exception handling
    #1)RuntimeError/LogicalError
    #2)SyntaxError
#Default exception Handling in Python
     #Every exception in python is an object.
     #terminates while handling problematic case.
'''
try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except ZeroDivisionError as use:
    print("This error is:",use)
except ValueError:
    print("please provide int value only")

    
try:
    x=int(input("Z: "))
    y=int(input("c: "))
    print(x/y)
except (ZeroDivisionError,ValueError,ArithmeticError) as use:
    print("kindy find your error in input:",use)
'''

