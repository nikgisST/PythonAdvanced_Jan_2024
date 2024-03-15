row = int(input())
flattened = []
for each_row in range(row):
    row_data = [int(x) for x in input().split(", ")]
    flattened.extend(row_data)
print(flattened)


row_count = int(input())
matrix = [map(int, input().split(", ")) for _ in range(row_count)]
flattened = [num for row in matrix for num in row]
print(flattened)


row = int(input())
matrix = []
for each_row in range(row):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)
flattened = []
for row in matrix:
    for el in row:
        flattened.append(el)
# flattened = [el for row in matrix for el in row]
print(flattened)