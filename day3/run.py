import re

def find_mul_pairs(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)
    return [(int(x), int(y)) for x, y in matches]


def find_mul_pairs_with_do_dont(text):
    parts = re.split(r"(don't\(\)|do\(\))", text)

    valid_muls = []

    ignore_next = False
    for part in parts:
        if part == "don't()":
            ignore_next = True
        elif part == "do()":
            ignore_next = False
        elif not ignore_next:
            pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
            matches = re.findall(pattern, part)
            valid_muls.extend([(int(x), int(y)) for x, y in matches])

    return valid_muls


with open("input.txt") as f:
    input_file = f.read()

part1 = 0
for (x, y) in find_mul_pairs(input_file):
    part1 += x * y

part2 = 0
for (x, y) in find_mul_pairs_with_do_dont(input_file):
    part2 += x * y


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")