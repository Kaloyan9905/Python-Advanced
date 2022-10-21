def age_assignment(*args, **kwargs):
    names = []
    final_res = []

    sorted_dict = sorted(kwargs.items(), key=lambda x: x[0], reverse=False)

    for name in args:
        names.append(name)

    for key, value in sorted_dict:
        for name in names:
            if name[0] == key:
                final_res.append(f"{name} is {value} years old.")

    return "\n".join(final_res)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))
