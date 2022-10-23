def is_inside(row, col, matrix_row, matrix_col):
    if 0 <= row < matrix_row and 0 <= col < matrix_col:
        return True
    return False



rows, cols = [int(x) for x in input().split(", ")]

matrix = []
santa_row, santa_col = 0, 0
steps = 0
end_program = False
counter = 0

items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0,
}

max_count_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0,
}

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for _ in range(rows):
    matrix.append(input().split())

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "Y":
            santa_row, santa_col = row, col
        elif matrix[row][col] == "D":
            max_count_items["Christmas decorations"] += 1
        elif matrix[row][col] == "C":
            max_count_items["Cookies"] += 1
        elif matrix[row][col] == "G":
            max_count_items["Gifts"] += 1

matrix[santa_row][santa_col] = "x"

while not end_program:

    command = input()

    if command == "End":
        break

    direction, steps = command.split("-")
    steps = int(steps)

    for key, value in positions.items():
        if direction == key:

            for index in range(steps):
                santa_row += value[0]
                santa_col += value[1]

                if not is_inside(santa_row, santa_col, rows, cols):
                    if direction == "left":
                        santa_col = cols - 1
                    elif direction == "right":
                        santa_col = 0
                    elif direction == "down":
                        santa_row = 0
                    elif direction == "up":
                        santa_row = rows - 1

                if matrix[santa_row][santa_col] == "D":
                    items["Christmas decorations"] += 1
                elif matrix[santa_row][santa_col] == "C":
                    items["Cookies"] += 1
                elif matrix[santa_row][santa_col] == "G":
                    items["Gifts"] += 1

                matrix[santa_row][santa_col] = "x"

                if items["Christmas decorations"] == max_count_items["Christmas decorations"]:
                    if items["Cookies"] == max_count_items["Cookies"]:
                        if items["Gifts"] == max_count_items["Gifts"]:
                            end_program = True
                            break

            if end_program:
                break

matrix[santa_row][santa_col] = "Y"

if end_program:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {items['Christmas decorations']} Christmas decorations")
print(f"- {items['Gifts']} Gifts")
print(f"- {items['Cookies']} Cookies")

for r in matrix:
    print(*r)