def fibonacci(n):
    """
    This function generates Fibonacci sequence up to a given number.
    Working:
    It starts with 0 and 1, then each next number is the sum of previous two numbers.
    Input:
    n (int) → limit up to which Fibonacci numbers are generated
    Output:
    Returns a list containing Fibonacci sequence up to n
    """
    a, b = 0, 1
    result = []
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result
print(fibonacci.__doc__)
print("Fibonacci:", fibonacci(10))