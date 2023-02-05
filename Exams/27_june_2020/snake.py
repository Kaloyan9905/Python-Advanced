def is_inside(row, col, length):
    return 0 <= row < length and 0 <= col < length


size = int(input())

matrix = [[x for x in list(input())] for _ in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

burrows_coordinates = []
snake_row, snake_col = 0, 0
total_food_eaten = 0
game_over = False

for row_index in range(size):
    for col_index in range(size):

        if matrix[row_index][col_index] == "S":
            snake_row, snake_col = row_index, col_index

        elif matrix[row_index][col_index] == "B":
            burrows_coordinates.append([row_index, col_index])

matrix[snake_row][snake_col] = "."

while total_food_eaten < 10 and not game_over:
    direction = input()

    for key, value in directions.items():
        if key == direction:
            snake_row += value[0]
            snake_col += value[1]

            if not is_inside(snake_row, snake_col, size):
                game_over = True
                break

            if matrix[snake_row][snake_col] == "-":
                matrix[snake_row][snake_col] = "."
                continue

            if matrix[snake_row][snake_col] == "*":
                matrix[snake_row][snake_col] = "."
                total_food_eaten += 1
                continue

            matrix[snake_row][snake_col] = "."

            for burrow_row, burrow_col in burrows_coordinates:
                if not snake_row == burrow_row and not snake_col == burrow_col:
                    snake_row, snake_col = burrow_row, burrow_col
                    matrix[snake_row][snake_col] = "."
if not game_over:
    matrix[snake_row][snake_col] = "S"

if game_over:
    print("Game over!")

if total_food_eaten >= 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {total_food_eaten}")

for r in matrix:
    print(*r, sep="")
