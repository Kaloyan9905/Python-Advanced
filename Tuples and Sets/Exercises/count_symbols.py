string = input()

my_dict = {}

for char in string:
    if char not in my_dict:
        my_dict[char] = 0
    my_dict[char] += 1

reworked_dict = sorted(my_dict.items(), key=lambda x: x[0])

[print(f"{key}: {value} time/s") for key, value in reworked_dict]