def is_inside(row, col, curr_size):
    return 0 <= row < curr_size and 0 <= col < curr_size


string = input()
size = int(input())

matrix = [[x for x in input()] for _ in range(size)]
matrix = list(matrix)

n = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

player_row, player_col = 0, 0

for index in range(size):
    if "P" in matrix[index]:
        player_row = index
        player_col = matrix[index].index("P")
        break

matrix[player_row][player_col] = "-"

for _ in range(n):
    position = input()

    for key, value in directions.items():
        if position == key:
            player_row += value[0]
            player_col += value[1]

            if is_inside(player_row, player_col, size):
                if matrix[player_row][player_col] == "-":
                    continue

                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = "-"
                continue

            player_row -= value[0]
            player_col -= value[1]

            if string:
                string = list(string)
                string.pop()
                string = "".join(string)

print(string)

matrix[player_row][player_col] = "P"

for r in matrix:
    print(*r, sep="")
