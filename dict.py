
student = {"name": "Alice", "age": 20, "grade": "A"}

print("Keys:", student.keys())
print("Values:", student.values())

student["city"] = "Delhi"

student["age"] = 21

del student["grade"]

print("Updated dictionary:", student)