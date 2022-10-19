rows, cols = [int(x) for x in input().split()]

for row in range(rows):
    counter = 0
    for col in range(cols):
        print(f"{chr(row + 97)}{chr(row + 97 + counter)}{chr(row + 97)}", end=" ")
        counter += 1
    print()

