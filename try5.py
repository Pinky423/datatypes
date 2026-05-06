try:
    f = open("data.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File does not exist")

finally:
    print("File handling done")