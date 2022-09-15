stack = []

n = int(input())

for _ in range(n):
    command = input()

    if "1" in command:
        stack.append(int(command.split()[1]))
    elif "2" in command:
        if stack:
            stack.pop()
    elif "3" in command:
        if stack:
            print(max(stack))
    else:
        if stack:
            print(min(stack))

if stack:
    while len(stack) - 1:
        print(stack.pop(), end=", ")

print(stack.pop())
