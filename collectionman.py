students = []
while True:

    print("\nWelcome to the Student Data Organizer!")
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\nEnter student details:")
        
        sid = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")
        
        student = {
            "id": sid,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }
        
        students.append(student)
        print("\nStudent added successfully!")
        
    elif choice == "2":
        print("\n--- Display All Students ---")

        if not students:
            print("No records found")
        else:
            for s in students:
                sub = ", ".join(s["subjects"])
                print(f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {sub}")
    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


