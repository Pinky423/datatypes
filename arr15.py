arr = [10, 20, 30, 40, 50]
x = int(input("Enter number: "))

found = False

for i in range(len(arr)):
    if arr[i] == x:
        print("Index:", i)
        found = True
        break

if not found:
    print("Not Found")