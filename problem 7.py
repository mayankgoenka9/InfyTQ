"""
Given a m x n matrix inmatrix of positive integers, print an integer outnum based on the below logic.

Identify all possible sets in inmatrix that contain at least four consecutive elements of the same value val, either horizontally, vertically, or diagonally
If only one set of consecutive elements is identified, store the value val in outnum
If more than one set of consecutive elements is identified, find the smallest value and store it in outnum
If no set of four consecutive elements of the same value is identified either horizontally, vertically, or diagonally, print-1

"""

r = int(input())
matrix = []
for _ in range(r):
    matrix.append(list(map(int, input().split())))
c = len(matrix[0])
result = []
for i in range(r):
    for j in range(c-3):
        if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]:
            if matrix[i][j] not in result:
                result.append(matrix[i][j])
                break
            else:
                pass
for i in range(r-3):
    for j in range(c):
        if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
            if matrix[i][j] not in result:
                result.append(matrix[i][j])
                break
            else:
                pass
for i in range(r-3):
    for j in range(c-3):
        if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]:
            if matrix[i][j] not in result:
                result.append(matrix[i][j])
                break
            else:
                pass
for i in range(r-3):
    for j in range(c+3):
        if matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2] == matrix[i+3][j-3]:
            if matrix[i][j] not in result:
                result.append(matrix[i][j])
                break
            else:
                pass

print(min(result))
