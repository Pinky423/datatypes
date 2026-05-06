# w mode
with open("modes.txt", "w") as f:
    f.write("Write mode")

# r mode
with open("modes.txt", "r") as f:
    print(f.read())

# a mode
with open("modes.txt", "a") as f:
    f.write("\nAppend mode")

# r+ mode
with open("modes.txt", "r+") as f:
    print(f.read())

# w+ mode
with open("modes.txt", "w+") as f:
    f.write("w+ mode")
    f.seek(0)
    print(f.read())

# a+ mode
with open("modes.txt", "a+") as f:
    f.write("\na+ mode")
    f.seek(0)
    print(f.read())