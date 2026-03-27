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
        sid = input("Enter Student ID to update: ")

        for s in students:
            if s["id"] == sid:
                s["name"] = input("New Name: ")
                s["age"] = input("New Age: ")
                s["grade"] = input("New Grade: ")
                print("Student updated!")
                break
        else:
            print("Student not found")

    elif choice == "4":
        sid = input("Enter Student ID to delete: ")

        students = [s for s in students if s["id"] != sid]
        print("Student deleted (if existed).")

    elif choice == "5":
        all_subjects = set()

        for s in students:
            all_subjects.update(s["subjects"])

        print("Subjects Offered:", ", ".join(all_subjects))
        
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")