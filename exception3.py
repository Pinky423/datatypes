# First create file
with open("sample3.txt", "w") as f:
    f.write("Line1\nLine2\nLine3")

# Read line by line
with open("sample3.txt", "r") as f:
    for line in f:
        print(line.strip())