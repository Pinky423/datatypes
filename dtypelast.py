students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}]
    
print("student name:")
for s in students:
    print(s["name"])
    
avg = sum(s["score"] for s in students) / len(students)
print("average score:",avg)

students.append({"id": 104, "name": "mickey", "score": 94})
print("new data:",students)

for s in students:
    if s["id"] == 102:
        s["score"] = 88
        
students = [s for s in students if s["name"] != "Charlie"]

print("Score > 80:") 
for s in students:
    if s["score"] > 80:
        print( s["name"])

sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)

top_student = max(students, key=lambda x: x["score"])
print("Highest scorer:", top_student["name"])

print("\nReport:")
for s in students:
    score = s["score"]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"

    print(f"Name: {s['name']} | Score: {score} | Grade: {grade}")

grade_count = {"A": 0, "B": 0, "C": 0}

for s in students:
    if s["score"] >= 90:
        grade_count["A"] += 1
    elif s["score"] >= 80:
        grade_count["B"] += 1
    else:
        grade_count["C"] += 1

print("Grade count:", grade_count)





