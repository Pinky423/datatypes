arr=[34,12,56,78,43,21,91]
while True:
    print("\nWelcome to the data analyzer and transformer program")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Dataset Statistics")
    print("7. Exit Program")

    choice=int(input("Please enter your choice:"))   

    if choice==1:
        print("Enter data for 1D Array:")
        print(arr)
        print("Data has been stored successfully!")

    elif choice==2:
        print("Data Summary:")
        print("Total Element:",len(arr))
        print("Minimum value:",min(arr))
        print("Maximum value:",max(arr))
        print("Sum:",sum(arr))
        print("Average:",sum(arr)/len(arr))
        
    elif choice==3:
        n = int(input("Enter number: "))
        fact = 1
        for i in range(1, n+1):
            fact *= i
        print("Factorial of",n,"is:", fact)

    elif choice==4:
        t = int(input("Enter a threshold value to filter out data above this value: "))
        res = []
        for i in arr:
            if i >= t:
                res.append(i)
        print("Filtered Data: ", res)   
    elif choice==5:
        print("Choose starting options:")
        print("1. Ascending")
        print("\n2. Descending")
        opt = int(input("Enter your choice: "))
        if opt == 1:
            arr.sort()
            print("Sorted:", arr)
        else:
            arr.sort(reverse=True)
            print("Sorted:", arr)

    elif choice==6:
        print("Minimum:", min(arr))
        print("Maximum:", max(arr))
        print("Sum:", sum(arr))
        print("Average:", sum(arr)/len(arr))

    elif choice==7:
        print("Thank you!")
        break   
    else:
        print("Invalid choice")