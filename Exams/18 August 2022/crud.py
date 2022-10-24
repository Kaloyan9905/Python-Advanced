matrix = []

for _ in range(6):
    matrix.append(input().split())

row, col = map(int, input().strip("(").strip(")").split(", "))

while True:

    line = input()

    if line == "Stop":
        for r in matrix:
            print(*r)
        break

    line = line.split(", ")

    if line[0] == "Create":
        direction, value = line[1], line[2]

        if direction == "left":
            col -= 1
            if not matrix[row][col] == ".":
                continue
            matrix[row][col] = value
        elif direction == "right":
            col += 1
            if not matrix[row][col] == ".":
                continue
            matrix[row][col] = value
        elif direction == "down":
            row += 1
            if not matrix[row][col] == ".":
                continue
            matrix[row][col] = value
        elif direction == "up":
            row -= 1
            if not matrix[row][col] == ".":
                continue
            matrix[row][col] = value

    elif line[0] == "Update":
        direction, value = line[1], line[2]

        if direction == "left":
            col -= 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = value
        elif direction == "right":
            col += 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = value
        elif direction == "down":
            row += 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = value
        elif direction == "up":
            row -= 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = value

    elif line[0] == "Delete":
        direction = line[1]

        if direction == "left":
            col -= 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = "."
        elif direction == "right":
            col += 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = "."
        elif direction == "down":
            row += 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = "."
        elif direction == "up":
            row -= 1
            if matrix[row][col] == ".":
                continue
            matrix[row][col] = "."

    elif line[0] == "Read":
        direction = line[1]

        if direction == "left":
            col -= 1
            if matrix[row][col] == ".":
                continue
        elif direction == "right":
            col += 1
            if matrix[row][col] == ".":
                continue
        elif direction == "down":
            row += 1
            if matrix[row][col] == ".":
                continue
        elif direction == "up":
            row -= 1
            if matrix[row][col] == ".":
                continue

        print(matrix[row][col])
