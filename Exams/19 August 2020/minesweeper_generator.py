def is_inside(r, c, length):
    return 0 <= r < length and 0 <= c < length


size = int(input())

matrix = []
bomb_coords = []

directions = {
    (1, 1),
    (-1, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (-1, 1),
    (1, -1),
}

for _ in range(size):
    matrix.append([0] * size)

n = int(input())

for _ in range(n):
    bomb = input()

    bomb_row, bomb_col = map(int, bomb.strip("(").strip(")").split(", "))

    matrix[bomb_row][bomb_col] = "*"
    bomb_coords.append([bomb_row, bomb_col])

for curr_row, curr_col in bomb_coords:

    for coords in directions:
        row_value, col_value = coords

        bomb_row, bomb_col = curr_row, curr_col

        bomb_row += row_value
        bomb_col += col_value

        if is_inside(bomb_row, bomb_col, size):
            if not matrix[bomb_row][bomb_col] == "*":
                matrix[bomb_row][bomb_col] += 1

for row in matrix:
    print(*row)
