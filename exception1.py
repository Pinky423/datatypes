with open("sample.txt", "w") as f:
    f.write("Hello Python")

with open("sample.txt", "r") as f:
    print(f.read())