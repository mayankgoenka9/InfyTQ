#Problem statement - To make every row and columne '0' where atleast one element is '0'
n = int(input())
matrix = []
zero_row = []
zero_col = []
for _ in range(n):
    matrix.append(list(map(int, input().strip())))

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 0:
            zero_row.append(i)
            zero_col.append(j)
        else:
            continue
for i in zero_row:
    for j in range(len(matrix)):
        matrix[i][j] = 0

for i in zero_col:
    for j in range(len(matrix)):
        matrix[j][i] = 0


for ele in matrix:
    print(ele)