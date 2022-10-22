def is_inside(row, col):
    if 0 <= row < 6 and 0 <= col < 6:
        return True
    return False


matrix = []
row_rover = 0
col_rover = 0
rover_gets_broken = False
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for _ in range(6):
    matrix.append(input().split())

commands = input().split(", ")

for r in range(6):
    for c in range(6):
        if matrix[r][c] == "E":
            row_rover, col_rover = r, c
            break

for command in commands:

    if command == "left":
        col_rover -= 1
    elif command == "right":
        col_rover += 1
    elif command == "down":
        row_rover += 1
    else:  # up
        row_rover -= 1

    if not is_inside(row_rover, col_rover):
        if command == "left":
            col_rover = 5
        elif command == "right":
            col_rover = 0
        elif command == "down":
            row_rover = 0
        else:  # up
            row_rover = 5

    if matrix[row_rover][col_rover] == "-":
        matrix[row_rover][col_rover] = "E"
        continue

    if matrix[row_rover][col_rover] == "W":
        matrix[row_rover][col_rover] = "E"
        water_deposit += 1
        print(f"Water deposit found at ({row_rover}, {col_rover})")
        continue

    if matrix[row_rover][col_rover] == "M":
        matrix[row_rover][col_rover] = "E"
        metal_deposit += 1
        print(f"Metal deposit found at ({row_rover}, {col_rover})")
        continue

    if matrix[row_rover][col_rover] == "C":
        matrix[row_rover][col_rover] = "E"
        concrete_deposit += 1
        print(f"Concrete deposit found at ({row_rover}, {col_rover})")
        continue

    print(f"Rover got broken at ({row_rover}, {col_rover})")
    rover_gets_broken = True
    break

if water_deposit and metal_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")