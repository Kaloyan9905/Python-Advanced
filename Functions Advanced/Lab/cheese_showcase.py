def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    res = ""

    for key, value in sorted_dict:
        res += key + '\n'
        sorted_values = sorted(value, reverse=True)
        res += '\n'.join([str(x) for x in sorted_values]) + '\n'

    return res


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
