def valid_indexes(row, col, mtrx):
    if 0 <= row < len(mtrx) and 0 <= col < len(mtrx):
        return True
    return False


r = int(input())

matrix = []

for _ in range(r):
    matrix.append([int(x) for x in input().split()])

command = input()

while not command == "END":
    command = command.split()

    if command[0] == "Add":
        if valid_indexes(int(command[1]), int(command[2]), matrix):
            r, c = int(command[1]), int(command[2])
            matrix[r][c] += int(command[3])
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        if valid_indexes(int(command[1]), int(command[2]), matrix):
            r, c = int(command[1]), int(command[2])
            matrix[r][c] -= int(command[3])
        else:
            print("Invalid coordinates")

    command = input()

for r in matrix:
    print(*r, sep=" ")
