def even_odd_filter(**kwargs):
    numbers_dict = {}

    for key, value in kwargs.items():
        if key not in numbers_dict:
            numbers_dict[key] = []
        if key == "odd":
            numbers_dict[key].extend([int(x) for x in value if not int(x) % 2 == 0])
        else:
            numbers_dict[key].extend([int(x) for x in value if int(x) % 2 == 0])

    reworked_dict = dict(sorted(numbers_dict.items(), key=lambda x: -len(x[1])))
    return reworked_dict



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
