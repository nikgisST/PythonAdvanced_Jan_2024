rows, columns = [int(x) for x in input().split()]

start = ord("a")

for row in range(start, start + rows):
    #print(chr(row))    --> a b c d
    for column in range(row, row + columns):
        print(chr(row), chr(column), chr(row), sep="", end=" ")
    print()