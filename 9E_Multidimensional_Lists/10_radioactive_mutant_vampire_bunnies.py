from collections import deque

FREE, BUNNY, PLAYER = ".", "B", "P"
DIRECTIONS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

rows, cols = [int(x) for x in input().split()]
row, col = None, None
bunnies = set()
field = []
for r in range(rows):
    line = list(input())
    for c in range(cols):
        if line[c] == PLAYER:
            row, col = r, c
        if line[c] == BUNNY:
            bunnies.add((r, c))
    field.append(line)

commands = deque(input())

end_game = False
player_won = False

while not end_game:
    command = commands.popleft()
    if command not in DIRECTIONS:
        continue
    r, c = DIRECTIONS[command]
    next_r, next_c = row + r, col + c
    if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
        end_game = True
        player_won = True
        field[row][col] = FREE

    elif field[next_r][next_c] == BUNNY:
        end_game = True
        field[row][col] = FREE
        row, col = next_r, next_c
    else:
        field[row][col] = FREE
        field[next_r][next_c] = PLAYER
        row, col = next_r, next_c

    for bunny_position in bunnies.copy():
        for direction in DIRECTIONS.values():
            r, c = direction
            row0, col0 = bunny_position
            next_r, next_c = row0 + r, col0 + c
            if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                continue
            if field[next_r][next_c] == PLAYER:
                player_won = False
                end_game = True
            field[next_r][next_c] = BUNNY
            bunnies.add((next_r, next_c))

[print(*line, sep="") for line in field]
if end_game and player_won:
    print(f"won: {row} {col}")
elif end_game and not player_won:
    print(f"dead: {row} {col}")





PLAYER, BUNNY, FREE = "P", "B", "."
directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
    "CURRENT": (0, 0)
}


def print_matrix(mtrx, sep=" "):
    for r in range(len(mtrx)):
        print(*mtrx[r], sep=sep)


def player_move(mtrx, player_pos, direction):
    r0, c0 = player_pos
    r1 = r0 + directions[direction][0]
    c1 = c0 + directions[direction][1]

    if r1 < 0 or r1 > len(mtrx) - 1 or c1 < 0 or c1 > len(mtrx[0]) - 1:
        mtrx[r0][c0] = FREE
        return f"won: {r0} {c0}"
    if mtrx[r1][c1] == BUNNY:
        mtrx[r0][c0] = FREE
        return f"dead: {r1} {c1}"
    mtrx[r1][c1], mtrx[r0][c0] = mtrx[r0][c0], mtrx[r1][c1]
    return r1, c1


def neighbours(mtrx, symbol):
    cells = set()
    for row in range(len(mtrx)):
        for col in range(len(mtrx[0])):
            if mtrx[row][col] == symbol:
                for direction, coordinates in directions.items():
                    x, y = coordinates
                    r, c = row + x, col + y
                    if 0 <= r <= len(mtrx) - 1 and 0 <= c <= len(mtrx[0]) - 1:
                        cells.add((r, c))
    return cells


def player_position(mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            if mtrx[i][j] == PLAYER:
                return i, j


def bunny_spread(mtrx):
    dead_pos = None
    positions = neighbours(mtrx, BUNNY)
    for pos in positions:
        x, y = pos
        if mtrx[x][y] == PLAYER:
            dead_pos = (x, y)
        mtrx[x][y] = BUNNY
    if dead_pos:
        return f"dead: {dead_pos[0]} {dead_pos[1]}"


rows, cols = [int(x) for x in input().split()]

field = [[x for x in input()] for _ in range(rows)]
commands = [x for x in input()]

position = player_position(field)
for command in commands:
    result = player_move(field, position, command)
    text = ""
    if type(result) == str:
        bunny_spread(field)
        print_matrix(field, sep="")
        print(result)
        break
    position = result
    spread_result = bunny_spread(field)
    if spread_result:
        print_matrix(field, sep="")
        print(spread_result)
        break
