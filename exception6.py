# Create file
with open("binary1.txt", "w") as f:
    f.write("Hello Binary")

# Read in binary
with open("binary1.txt", "rb") as f:
    data = f.read()
    print(data)