matrix = [[3,5,1],[8,2,7],[4,9,6]]

max_val = matrix[0][0]
min_val = matrix[0][0]


for row in matrix:
    for val in row:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val

print("Max:", max_val)
print("Min:", min_val)