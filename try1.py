try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result=a/b
except ZeroDivisionError:
    print("cant divide by zero")
else:
    print("result:",result)