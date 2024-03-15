row, column = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split(", ")])

total_sum = 0
max_number = float('-inf')
submatrix = []

for row_index in range(row - 1):
    for column_index in range(column - 1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        under_element = matrix[row_index + 1][column_index ]
        diagonal_element = matrix[row_index + 1][column_index + 1]

        total_sum = current_element + next_element + under_element + diagonal_element

        if max_number < total_sum:
            max_number = total_sum
            submatrix = [[current_element, next_element], [under_element, diagonal_element]]

print(*submatrix[0])
print(*submatrix[1])
print(max_number)

