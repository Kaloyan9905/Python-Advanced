from collections import deque

string = deque(input().split())

numbers = deque()
final_result = deque()
operator = None

while True:
    char = string.popleft()

    if char not in "-*/+":
        numbers.append(int(char))
        continue

    operator = char
    result = numbers.popleft()

    while numbers:
        number = numbers.popleft()

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number
        elif operator == "*":
            result *= number
        else:
            result //= number

    string.appendleft(str(result))

    if len(string) == 1:
        break

print(*string)

