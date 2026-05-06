try:
    filename = input("Enter filename: ")
    f = open(filename, "r")

except FileNotFoundError:
    print("File not found")

else:
    print("File content:")
    print(f.read())
    f.close()