class Grandparent:
    pass
class Parent(Grandparent):
    pass
class Child(Parent):
    pass
print(issubclass(Child,Parent))
print(issubclass(Child,Grandparent))