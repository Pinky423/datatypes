def write_file():
    f = open("demo.txt", "w")
    f.write("Hello")
    f.close()

def read_file():
    f = open("demo.txt", "r")
    print(f.read())
    f.close()