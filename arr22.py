matrix=[[1,2,3],[4,5,6]]
transpose=[]
for j in range(3):
    row=[]
    for i in range(2):
        row.append(matrix[i][j])
    transpose.append(row)
for row in transpose:
    print(row)