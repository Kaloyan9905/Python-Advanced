n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(input()))

symbol = input()

for row in range(n):
    for column in range(n):
        if matrix[row][column] == symbol:
            print(f"({row}, {column})")
            exit()

print(f"{symbol} does not occur in the matrix")
