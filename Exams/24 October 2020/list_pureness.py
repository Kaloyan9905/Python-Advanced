from collections import deque


def best_list_pureness(*args):
    rotations = args[-1]
    numbers = deque([str(x) for x in args[0]])

    best_rotation = None
    best_result = float("-inf")

    for index in range(rotations):
        current_result = 0
        counter = 0

        for number in numbers:
            current_result += counter * int(number)
            counter += 1

        if current_result > best_result:
            best_result = current_result
            best_rotation = index

        numbers.appendleft(numbers.pop())

    return f"Best pureness {best_result} after {best_rotation} rotations"


test = ([1, 2, 3], 10)
result = best_list_pureness(*test)
print(result)
