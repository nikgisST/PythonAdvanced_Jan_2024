rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
biggest_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        first_row = matrix[row][column:column + 3]
        second_row = matrix[row + 1][column:column + 3]
        third_row = matrix[row + 2][column:column + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_row,
                              second_row,
                              third_row]
            # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_matrix]
#print(1, 2, 3)         -->    1 2 3
#print(+[1, 2, 3])      -->    1 2 3