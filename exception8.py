with open("modify.txt", "w") as f:
    f.write("Original content\n")

with open("modify.txt", "r+") as f:
    print(f.read())
    f.write("This file was last modified by adding this sentence.\n")