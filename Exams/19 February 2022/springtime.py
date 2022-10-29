def start_spring(**kwargs):
    my_dict = {}
    res = ""

    for key, value in kwargs.items():
        if value not in my_dict:
            my_dict[value] = []
        my_dict[value].append(key)

    reworked_dict = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in reworked_dict:
        res += f"{key}:" + "\n"
        value.sort()
        for v in value:
            res += f"-{v}" + "\n"

    return res


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

