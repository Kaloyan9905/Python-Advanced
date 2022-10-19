def valid_coords(mtrx, cell_row, cell_col, neighbours):
    if is_inside(mtrx, cell_row + 1, cell_col):  # yes
        neighbours.append([cell_row + 1, cell_col])

    if is_inside(mtrx, cell_row - 1, cell_col):  # yes
        neighbours.append([cell_row - 1, cell_col])

    if is_inside(mtrx, cell_row + 1, cell_col + 1):  # yes
        neighbours.append([cell_row + 1, cell_col + 1])

    if is_inside(mtrx, cell_row + 1, cell_col - 1):  # yes
        neighbours.append([cell_row + 1, cell_col - 1])

    if is_inside(mtrx, cell_row - 1, cell_col - 1):  # yes
        neighbours.append([cell_row - 1, cell_col - 1])

    if is_inside(mtrx, cell_row - 1, cell_col + 1):  # yes
        neighbours.append([cell_row - 1, cell_col + 1])

    if is_inside(mtrx, cell_row, cell_col + 1):  # yes
        neighbours.append([cell_row, cell_col + 1])

    if is_inside(mtrx, cell_row, cell_col - 1):  # yes
        neighbours.append([cell_row, cell_col - 1])

    return neighbours


def is_inside(mtrx, cell_row, cell_col):
    if 0 <= cell_row < len(mtrx) and 0 <= cell_col < len(mtrx):
        return True
    return False


n = int(input())

matrix = []
all_side_cells = []
alive_cells = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

coords = input().split()

for coord in coords:
    row, col = [int(x) for x in coord.split(",")]

    if matrix[row][col] <= 0:
        continue

    all_side_cells = valid_coords(matrix, row, col, all_side_cells)

    for curr_row, curr_col in all_side_cells:
        if matrix[curr_row][curr_col] > 0:
            matrix[curr_row][curr_col] -= matrix[row][col]

    all_side_cells.clear()
    matrix[row][col] = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells.append(matrix[row][col])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for r in matrix:
    print(*r)
