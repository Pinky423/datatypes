import uuid

students = {
    "101": uuid.uuid4(),
    "102": uuid.uuid4(),
    "103": uuid.uuid4()
}

for k, v in students.items():
    print(k, ":", v)