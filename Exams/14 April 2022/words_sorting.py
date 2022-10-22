def words_sorting(*args):
    my_dict = {}
    total_sum = 0
    result = ""

    for word in args:
        sum_nums = 0
        my_dict[word] = 0

        for char in word:
            sum_nums += ord(char)

        my_dict[word] += sum_nums
        total_sum += sum_nums

    if total_sum % 2 == 0:
        reworked_dict = sorted(my_dict.items(), key=lambda x: x[0])
    else:
        reworked_dict = sorted(my_dict.items(), key=lambda x: -x[1])

    for key, value in reworked_dict:
        result += f"{key} - {value}" + "\n"

    return result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))


