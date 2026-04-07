count = 0

def fun():
    global count
    count += 1
    print("Function called", count, "times")

fun()
fun()
fun()