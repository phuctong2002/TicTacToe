CELL_SIZE = 55
COLUMN = 10
ROW = 10
WIDTH = 800
HEIGHT = 600
step = 0

matrix = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    matrix.append(row)

print(matrix[1][1])
