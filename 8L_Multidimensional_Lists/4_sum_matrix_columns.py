row, column = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(row):
    row_nums = [int(el) for el in input().split()]
    matrix.append(row_nums)

for column_index in range(0, column):
    column_total_sum = 0
    for row_index in range(row):
        column_total_sum += matrix[row_index][column_index]
    print(column_total_sum)