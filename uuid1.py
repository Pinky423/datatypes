import uuid

u1 = uuid.uuid4()
print("Random UUID:", u1)

u2 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
