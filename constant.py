CELL_SIZE = 55
COLUMN = 10
ROW = 10
WIDTH = 800
HEIGHT = 600
step = 0
# step chan la nguoi di le la may di
matrix = []
# 0 la chua di 1 la may di -1 la may nguoi
# chien luoc la may thang tuong duong voi viec nguoi chon min may chon max
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    matrix.append(row)

