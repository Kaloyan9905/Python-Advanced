def strongest_nums(pos, neg):
    if pos > abs(neg):
        return "The positives are stronger than the negatives"
    return "The negatives are stronger than the positives"



nums = [int(x) for x in input().split()]

positive_nums_sum = sum([int(x) for x in nums if x > 0])
negative_nums_sum = sum([int(x) for x in nums if x < 0])

print(negative_nums_sum)
print(positive_nums_sum)
print(strongest_nums(positive_nums_sum, negative_nums_sum))
