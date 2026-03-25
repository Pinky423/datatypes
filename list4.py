squares = [x*x for x in range(1, 11)]
print("Squares:", squares)

even_nums = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", even_nums)

words = ["hello", "WORLD", "PyThOn"]

lower_words = [w.lower() for w in words]
print("Lowercase:", lower_words)