def add_first(first, args):
    for char in args:
        first.add(char)

    return first


def add_second(second, args):
    for char in args:
        second.add(char)

    return second


def remove_first(first, args):
    for ele in args:
        if ele in first:
            first.remove(ele)

    return first


def remove_second(second, args):
    for ele in args:
        if ele in second:
            second.remove(ele)

    return second


def is_subset(first, second):
    if first.issubset(second) or second.issubset(first):
        return "True"
    return "False"


first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    command = input()

    if "Add First" in command:
        first_sequence = add_first(first_sequence, [int(x) for x in command.split()[2::]])
    elif "Add Second" in command:
        second_sequence = add_second(second_sequence, [int(x) for x in command.split()[2::]])
    elif "Remove First" in command:
        first_sequence = remove_first(first_sequence, [int(x) for x in command.split()[2::]])
    elif "Remove Second" in command:
        second_sequence = remove_second(second_sequence, [int(x) for x in command.split()[2::]])
    else:  # Check Subset
        print(is_subset(first_sequence, second_sequence))

first_sequence = list(first_sequence)
second_sequence = list(second_sequence)

first_sequence.sort()
second_sequence.sort()

print(', '.join([str(x) for x in first_sequence]))
print(', '.join([str(x) for x in second_sequence]))

