def cube_list(lst):
    result = []
    for i in lst:
        result.append(i**3)
    return result

numbers = [6, 3, 1, 2]
print(cube_list(numbers))