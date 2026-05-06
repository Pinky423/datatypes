import math

try:
    num = int(input("Enter number: "))
    if num < 0:
        raise ValueError("Negative number")

    result = math.sqrt(num)

except ValueError:
    print("Error: Cannot find square root of negative number")

else:
    print("Square root:", result)

finally:
    print("Execution complete.")