def print_name(*names):
    if not names:
        print("List is empty")
    else:
        for name in names:
            print(name)
print_name("Alice","Bob","john")
