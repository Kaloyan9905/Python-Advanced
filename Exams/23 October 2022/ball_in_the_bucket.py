matrix = []
result = 0

for r in range(6):
    matrix.append(input().split())

for _ in range(3):
    coords = input()

    coords = coords.replace("(", "")
    coords = coords.replace(")", "")

    row, col = [int(x) for x in coords.split(", ")]

    if row > 5 or col > 5:
        continue

    if not matrix[row][col] == "B":
        continue

    matrix[row][col] = "X"

    for c in matrix:
        result += int(c[col]) if c[col] != "B" and c[col] != "X" else 0

if result < 100:
    print(f"Sorry! You need {100 - result} points more to win a prize.")
else:
    if 100 <= result <= 199:
        prize = "Football"
    elif 200 <= result <= 299:
        prize = "Teddy Bear"
    else:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {result} points, and you've won {prize}.")
