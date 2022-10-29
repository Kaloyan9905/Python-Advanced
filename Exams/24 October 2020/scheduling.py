from collections import deque

numbers = deque([int(x) for x in input().split(", ")])
index = int(input())

needed_job = numbers[index]
total_cycles = 0

total_needed_jobs = numbers.count(needed_job)

while total_needed_jobs:

    current_number = min(numbers)
    numbers.remove(current_number)

    total_cycles += current_number

    if current_number == needed_job:
        total_needed_jobs -= 1

print(total_cycles)


