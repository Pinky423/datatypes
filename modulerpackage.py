import math
import random
import uuid
import time
from datetime import datetime
print("Welcome to Multi-Utility Toolkit")

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            now = datetime.now()
            print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == '2':
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.strptime(d2, "%Y-%m-%d")

            diff = abs((date2 - date1).days)
            print("Difference:", diff, "days")

        elif choice == '3':
            now = datetime.now()
            print(now.strftime("%d-%m-%Y"))
            print(now.strftime("%I:%M:%S %p"))

        elif choice == '4':
            input("Press Enter to Start Stopwatch")
            start = time.time()

            input("Press Enter to Stop Stopwatch")
            end = time.time()

            print("Elapsed Time:", int(end - start), "seconds")

        elif choice == '5':
            sec = int(input("Enter seconds: "))

            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1

            print("Time's Up!")

        elif choice == '6':
            break

        else:
            print("Invalid Choice")

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("Enter a number: "))
            print("Factorial:", math.factorial(n))

        elif choice == '2':
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (%): "))
            t = float(input("Enter time (in years): "))

            ci = p * ((1 + r / 100) ** t)
            print("Compound Interest:", round(ci, 2))

        elif choice == '3':
            angle = int(input("Enter angle in degrees: "))
            rad = math.radians(angle)

            print("Sin:", math.sin(rad))
            print("Cos:", math.cos(rad))
            print("Tan:", math.tan(rad))

        elif choice == '4':
            r = float(input("Enter radius of circle: "))
            area = math.pi * r * r
            print("Area of Circle:", area)

        elif choice == '5':
            break

        else:
            print("Invalid Choice")

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Random Number:", random.randint(1, 100))

        elif choice == '2':
            nums = []
            for i in range(5):
                nums.append(random.randint(1, 100))

            print(nums)

        elif choice == '3':
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%"
            length = int(input("Enter password length: "))

            password = ""
            for i in range(length):
                password += random.choice(chars)

            print("Generated Password:", password)

        elif choice == '4':
            otp = random.randint(1000, 9999)
            print("Generated OTP:", otp)

        elif choice == '5':
            break

        else:
            print("Invalid Choice")

def uuid_menu():
    while True:
        print("\nGenerate Unique Identifiers (UUID):")
        print("1. Generate UUID")
        print("2. Generate UUID using namespace")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Generated UUID:", uuid.uuid4())

        elif choice == '2':
            name = input("Enter name: ")
            print(uuid.uuid5(uuid.NAMESPACE_DNS, name))

        elif choice == '3':
            break

        else:
            print("Invalid Choice")

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            fname = input("Enter file name: ")
            open(fname, 'w').close()
            print("File created successfully!")

        elif choice == '2':
            fname = input("Enter file name: ")
            data = input("Enter data to write: ")

            with open(fname, 'w') as f:
                f.write(data)

            print("Data written successfully!")

        elif choice == '3':
            fname = input("Enter file name: ")

            with open(fname, 'r') as f:
                print("File Content:")
                print(f.read())

        elif choice == '4':
            fname = input("Enter file name: ")
            data = input("Enter data to append: ")

            with open(fname, 'a') as f:
                f.write(data)

            print("Data appended successfully!")

        elif choice == '5':
            break

        else:
            print("Invalid Choice")

def explore_menu():
    module = input("Enter module name to explore: ")

    try:
        mod = __import__(module)
        print("Available Attributes in", module, "module:")
        print(dir(mod))

    except:
        print("Module not found")

while True:
    print("\n============================")
    print("Welcome to Multi-Utility Toolkit")
    print("============================")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("============================")

    choice = input("Enter your choice: ")

    if choice == '1':
        datetime_menu()

    elif choice == '2':
        math_menu()

    elif choice == '3':
        random_menu()

    elif choice == '4':
        uuid_menu()

    elif choice == '5':
        file_menu()

    elif choice == '6':
        explore_menu()

    elif choice == '7':
        print("Thank you for using the Multi-Utility Toolkit!")
        break

    else:
        print("Invalid Choice")