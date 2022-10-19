def is_inside(mtrx_row, mtrx_col, p_row, p_col):
    if 0 <= p_row < mtrx_row and 0 <= p_col < mtrx_col:
        return True
    return False


rows, cols = [int(x) for x in input().split()]

matrix = []
player_row, player_col = 0, 0
dead = False
won = False

for _ in range(rows):
    matrix.append(list(input()))

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "P":
            player_row, player_col = row, col
            break

commands = input()

for command in commands:
    bunnies = []
    matrix[player_row][player_col] = "."

    if command == "L":
        player_col -= 1
    elif command == "R":
        player_col += 1
    elif command == "U":
        player_row -= 1
    else:  # D
        player_row += 1

    if not is_inside(rows, cols, player_row, player_col):
        won = True

        if command == "L":
            player_col += 1
        elif command == "R":
            player_col -= 1
        elif command == "U":
            player_row += 1
        else:  # D
            player_row -= 1

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "B":
                    bunnies.append([row, col])

        for bunny_row, bunny_col in bunnies:
            if is_inside(rows, cols, bunny_row + 1, bunny_col):
                matrix[bunny_row + 1][bunny_col] = "B"

            if is_inside(rows, cols, bunny_row - 1, bunny_col):
                matrix[bunny_row - 1][bunny_col] = "B"

            if is_inside(rows, cols, bunny_row, bunny_col + 1):
                matrix[bunny_row][bunny_col + 1] = "B"

            if is_inside(rows, cols, bunny_row, bunny_col - 1):
                matrix[bunny_row][bunny_col - 1] = "B"

        if won:
            break

    matrix[player_row][player_col] = "P"

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                bunnies.append([row, col])

    for bunny_row, bunny_col in bunnies:
        if is_inside(rows, cols, bunny_row + 1, bunny_col):
            matrix[bunny_row + 1][bunny_col] = "B"

            if bunny_row + 1 == player_row and bunny_col == player_col:
                dead = True

        if is_inside(rows, cols, bunny_row - 1, bunny_col):
            matrix[bunny_row - 1][bunny_col] = "B"

            if bunny_row - 1 == player_row and bunny_col == player_col:
                dead = True

        if is_inside(rows, cols, bunny_row, bunny_col + 1):
            matrix[bunny_row][bunny_col + 1] = "B"

            if bunny_row == player_row and bunny_col + 1 == player_col:
                dead = True

        if is_inside(rows, cols, bunny_row, bunny_col - 1):
            matrix[bunny_row][bunny_col - 1] = "B"

            if bunny_row == player_row and bunny_col - 1 == player_col:
                dead = True

    if dead or won:
        break


for r in matrix:
    print(*r, sep="")

if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")








