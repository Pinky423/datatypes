def employee_details(**kwargs):
    required = ["name", "department", "salary"]
    
    for field in required:
        if field not in kwargs:
            print(f"{field} is missing")
            return required
    
    print("Employee Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

employee_details(name="Pinky", department="IT", salary=30000)