numbers = [float(x) for x in input().split()]

numbers_dict = {}

for number in numbers:
    if number not in numbers_dict:
        numbers_dict[number] = 0
    numbers_dict[number] += 1

[print(f'{float(key)} - {value} times') for key, value in numbers_dict.items()]