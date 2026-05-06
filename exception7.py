with open("count.txt", "w") as f:
    f.write("Python is easy\nPython is powerful")

with open("count.txt", "r") as f:
    content = f.read()
    
    words = len(content.split())
    chars = len(content)
    lines = content.count("\n") + 1

print("Words:", words)
print("Characters:", chars)
print("Lines:", lines)