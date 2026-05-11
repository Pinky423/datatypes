import uuid

u1 = uuid.uuid4()
u2 = uuid.uuid4()

print("UUID1:", u1)
print("UUID2:", u2)

if u1 == u2:
    print("Equal")
else:
    print("Not Equal")