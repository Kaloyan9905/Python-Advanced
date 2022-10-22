import math


def is_inside(row, col, matrix_size):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True
    return False


size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]

path = []
coins = 0
player_row, player_col = 0, 0
win = False
lose = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for index in range(size):
    if "P" in matrix[index]:
        player_row = index
        player_col = matrix[index].index("P")
        break

path.append([player_row, player_col])
matrix[player_row][player_col] = "E"

while True:
    if win or lose:
        break

    command = input()

    for key, value in directions.items():
        if key == command:
            player_row += value[0]
            player_col += value[1]

            if not is_inside(player_row, player_col, size):
                if command == "left":
                    player_col = size - 1
                elif command == "right":
                    player_col = 0
                elif command == "up":
                    player_row = size - 1
                else:
                    player_row = 0

            if matrix[player_row][player_col] == "X":
                path.append([player_row, player_col])
                lose = True
                break

            if matrix[player_row][player_col] == "E":
                path.append([player_row, player_col])
                continue

            coins += int(matrix[player_row][player_col])
            path.append([player_row, player_col])
            matrix[player_row][player_col] = "E"

            if coins >= 100:
                win = True
                break

if win and coins >= 100:
    print(f"You won! You've collected {coins} coins.")
if lose:
    print(f"Game over! You've collected {math.floor(coins / 2)} coins.")

print(f"Your path:")
for current_path in path:
    print(current_path)
