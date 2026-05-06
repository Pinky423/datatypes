try:
    s = "Hello"
    print(s[8])

except IndexError:
    print("Error: Invalid string index")

else:
    print("Character accessed successfully")