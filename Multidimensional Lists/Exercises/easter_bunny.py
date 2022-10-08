def is_inside(num, r, c):
    if 0 <= r < num and 0 <= c < num:
        return True
    return False


size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]

bunny_row, bunny_col = 0, 0
best_direction = ""
best_direction_sum = 0

positions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

positions_data = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}

positions_data_indexes = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}

directions = [
    "right",
    "left",
    "down",
    "up",
]

for index in range(size):
    if "B" in matrix[index]:
        bunny_row, bunny_col = index, matrix[index].index("B")
        break

while directions:
    for direction in positions:
        curr_row, curr_col = bunny_row, bunny_col
        curr_direction = directions.pop()

        while is_inside(size, curr_row + direction[0], curr_col + direction[1]):
            curr_row += direction[0]
            curr_col += direction[1]

            if matrix[curr_row][curr_col] == "X":
                break

            for key, value in positions_data.items():
                if key == curr_direction:
                    value.append(int(matrix[curr_row][curr_col]))
                    positions_data_indexes[key].append([curr_row, curr_col])
                    break

reworked_positions_data = sorted(positions_data.items(), key=lambda x: -sum(x[1]))

for key, value in reworked_positions_data:
    if value:
        best_direction = key
        best_direction_sum += sum(value)
        break

print(best_direction)

for key, value in positions_data_indexes.items():
    if key == best_direction:
        for v in value:
            print(v)

print(best_direction_sum)
