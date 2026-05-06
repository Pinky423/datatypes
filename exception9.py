with open("search.txt", "w") as f:
    f.write("Python is great\nLearning Python is fun")

word = input("Enter word to search: ")

with open("search.txt", "r") as f:
    for i, line in enumerate(f, 1):
        if word in line:
            print("Found in line:", i)