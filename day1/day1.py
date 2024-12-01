from collections import Counter

with open("day1.txt") as f:
    lists = f.read().splitlines()
    
first_col, second_col = [], []

for line in lists:
    first, second = line.split("   ")
    first = int(first)
    second = int(second)
    first_col.append(first)
    second_col.append(second)

first_col.sort()
second_col.sort()

total_dist = 0

for first, second in zip(first_col, second_col):
    total_dist += abs(first - second)

print(f"Part 1: {total_dist}")

# Part 2
part_two_total = 0

second_col_collection = Counter(second_col)
for item in first_col:
    part_two_total += item * second_col_collection[item]

print(f"Part 2: {part_two_total}")