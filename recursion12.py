value = 0
def initialize():
    global value
    value=10
def increment(x):
    global value
    value+=x
initialize()
increment(4)
print(value)