rows, columns = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]       # [[0, 0, 0], ....]

equal_blocks = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        symbol = matrix[row][column]

        if symbol == matrix[row + 1][column] and symbol == matrix[row][column + 1] \
            and symbol == matrix[row + 1][column + 1]:
            equal_blocks += 1

print(equal_blocks)




rows, columns = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]       # [[0, 0, 0], ....]

equal_blocks = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        symbol = matrix[row][column]

        valid_block = True

        for inner_row in range(row, row + 2):
            for inner_column in range(column, column + 2):
                if symbol != matrix[inner_row][inner_column]:
                    valid_block = False
                    break
                    
            if not valid_block:
                break
        else:
            equal_blocks += 1

print(equal_blocks)

