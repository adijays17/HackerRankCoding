def setZeroes(matrix):
    row = []
    col = []
    l_row = len(matrix)
    l_col = len(matrix[0])
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    for each in row:
        for e in range(0, l_col):
            matrix[each][e] = 0
    for cach in col:
        for c in range(0, l_row):
            matrix[c][cach] = 0
    return matrix

print(setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))