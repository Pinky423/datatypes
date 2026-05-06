with open("source.txt", "w") as f:
    f.write("Backup this data")

with open("source.txt", "r") as f1:
    data = f1.read()

with open("backup.txt", "w") as f2:
    f2.write(data)