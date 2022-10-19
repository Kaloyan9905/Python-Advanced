rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()

    if command == "END":
        break

    command = command.split()
    condition = True

    if not command[0] == "swap":
        print("Invalid input!")
        continue

    if not len(command) == 5:
        print("Invalid input!")
        continue

    for cmd in command[1::]:
        if int(cmd) > rows or int(cmd) > cols or int(cmd) < 0:
            print("Invalid input!")
            condition = False
            break

    if not condition:
        continue

    row1, col1 = int(command[1]), int(command[2])
    row2, col2 = int(command[3]), int(command[4])

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for i in range(len(matrix)):
        print(*matrix[i])
