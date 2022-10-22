def flights(*args):
    my_dict = {}

    for index in range(len(args) - 1):
        if args[index] == "Finish":
            break
        if index % 2 == 0:
            if args[index] not in my_dict:
                my_dict[args[index]] = 0
            my_dict[args[index]] += int(args[index + 1])

    return my_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
