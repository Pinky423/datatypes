num = int(input("Enter number: "))

if num < 0:
    raise ValueError("Negative number not allowed")

print("Valid number:", num)