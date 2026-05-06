# Create + write
with open("sample2.txt", "w") as f:
    f.write("Old content")

# Read
with open("sample2.txt", "r") as f:
    print(f.read())

# Overwrite
with open("sample2.txt", "w") as f:
    f.write("Learning file handling in Python is fun!")
