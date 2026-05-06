# Create file first
with open("notes2.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# Append
with open("notes2.txt", "a") as f:
    f.write("Line 4: Python supports multiple modes of file handling.\n")