username = "guest"

def update_name():
    global username
    username = input("Enter new name: ")

update_name()
print("Updated name:", username)