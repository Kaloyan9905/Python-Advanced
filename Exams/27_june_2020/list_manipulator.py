from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)

    if args[0] == "add" and args[1] == "beginning":
        index = 0

        for number in args[2::]:
            numbers.insert(index, number)
            index += 1

    elif args[0] == "add" and args[1] == "end":
        numbers.extend(args[2::])

    elif args[0] == "remove" and args[1] == "beginning":
        if len(args) > 2:
            for _ in range(args[2]):
                numbers.popleft()
        else:
            numbers.popleft()

    elif args[0] == "remove" and args[1] == "end":
        if len(args) > 2:
            for _ in range(args[2]):
                numbers.pop()
        else:
            numbers.pop()

    return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
