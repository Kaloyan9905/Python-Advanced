def numbers_searching(*args):
    duplicates_dict = {}
    duplicates_list = []
    result = []
    missing_number = None

    for number in args:
        if number not in duplicates_dict:
            duplicates_dict[number] = 0
        duplicates_dict[number] += 1

    for key, value in duplicates_dict.items():
        if value > 1:
            duplicates_list.append(key)

    duplicates_list.sort()

    start = min(args)
    end = max(args)

    for index in range(start, end + 1):
        if index not in args:
            missing_number = index

    result.append(missing_number)
    result.append(duplicates_list)

    return result



print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
