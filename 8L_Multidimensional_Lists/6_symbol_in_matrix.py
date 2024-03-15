n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

searched_element = input()

for row_index in range(n):
    for column_index in range(len(matrix[row_index])):
        if matrix[row_index][column_index] == searched_element:
            print(f"({row_index}, {column_index})")
            exit()
print(f"{searched_element} does not occur in the matrix")





n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

searched_element = input()
is_found = False

for row_index in range(n):
    if is_found:
        break
    for column_index in range(len(matrix[row_index])):
        if matrix[row_index][column_index] == searched_element:
            print(f"({row_index}, {column_index})")
            is_found = True
            break

if not is_found:
    print(f"{searched_element} does not occur in the matrix")




size = int(input())
matrix_of_chars = []

for _ in range(0, size):
    matrix_of_chars.append(list(input()))

symbol = input()
location = ()
found = False

for row in range(0, size):
    if found:
        break
    for column in range(0, size):
        if matrix_of_chars[row][column] == symbol:
            location = (row, column)
            found = True
if found:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")