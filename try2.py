try:
    lst = [10, 20, 30]
    print(lst[5])   # invalid index

except IndexError:
    print("Error: Index does not exist")