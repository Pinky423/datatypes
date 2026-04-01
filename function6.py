def calc(*args):
    total = sum(args)
    product = 1
    for i in args:
        product *= i
    return total,product
print(calc(1,4,5,2,7))