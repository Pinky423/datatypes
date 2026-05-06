try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print("Result:", a / b)

except:
    print("Invalid input or division by zero")

finally:
    print("Program finished")