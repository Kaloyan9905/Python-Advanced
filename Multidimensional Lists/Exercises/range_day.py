def is_inside(curr_row, curr_col):
    if 0 <= curr_row < 5 and 0 <= curr_col < 5:
        return True
    return False


matrix = []
shooter_row, shooter_col = 0, 0
total_targets = 0
dead_targets = []

for _ in range(5):
    matrix.append(input().split())

for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            shooter_row, shooter_col = row, col
        elif matrix[row][col] == "x":
            total_targets += 1

n = int(input())

for _ in range(n):
    command = input().split()

    temp_row, temp_col = shooter_row, shooter_col

    if command[0] == "shoot":
        direction = command[1]

        while True:
            if direction == "left":
                temp_col -= 1
            elif direction == "right":
                temp_col += 1
            elif direction == "up":
                temp_row -= 1
            else:
                temp_row += 1

            if is_inside(temp_row, temp_col):
                if matrix[temp_row][temp_col] == "x":
                    dead_targets.append([temp_row, temp_col])
                    matrix[temp_row][temp_col] = "."
                    break
            else:
                break

        if len(dead_targets) == total_targets:
            break

    elif command[0] == "move":
        direction, steps = command[1], int(command[2])

        matrix[shooter_row][shooter_col] = "."

        if direction == "left":
            shooter_col -= steps

            if is_inside(shooter_row, shooter_col) and matrix[shooter_row][shooter_col] == ".":
                matrix[shooter_row][shooter_col] = "A"
            else:
                shooter_col += steps
                matrix[shooter_row][shooter_col] = "A"

        elif direction == "right":
            shooter_col += steps

            if is_inside(shooter_row, shooter_col) and matrix[shooter_row][shooter_col] == ".":
                matrix[shooter_row][shooter_col] = "A"
            else:
                shooter_col -= steps
                matrix[shooter_row][shooter_col] = "A"

        elif direction == "up":
            shooter_row -= steps

            if is_inside(shooter_row, shooter_col) and matrix[shooter_row][shooter_col] == ".":
                matrix[shooter_row][shooter_col] = "A"
            else:
                shooter_row += steps
                matrix[shooter_row][shooter_col] = "A"

        else:
            shooter_row += steps

            if is_inside(shooter_row, shooter_col) and matrix[shooter_row][shooter_col] == ".":
                matrix[shooter_row][shooter_col] = "A"
            else:
                shooter_row -= steps
                matrix[shooter_row][shooter_col] = "A"

if len(dead_targets) == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - len(dead_targets)} targets left.")

if dead_targets:
    print('\n'.join(f"[{row}, {column}]" for row, column in dead_targets))


