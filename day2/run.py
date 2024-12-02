import numpy
test_input = [
    '7 6 4 2 1',
    '1 2 7 8 9',
    '9 7 6 2 1',
    '1 3 2 4 5',
    '8 6 4 4 1',
    '1 3 6 7 9',
]
def check_report(nums: numpy.array) -> bool:
    first_diff = nums[1:] - nums[:-1]
    all_inc_or_decr = all(first_diff > 0) or all(first_diff < 0)
    any_large_diffs = numpy.any(numpy.abs(first_diff) > 3)

    # If all increasing or decreasing and no large differences, add it
    if all_inc_or_decr and not any_large_diffs:
        return True
    return False

with open ("input.txt") as f:
    input_file = f.read().splitlines()

# Part 1
safe_reports_1 = 0
safe_reports_2 = 0
for report in input_file:
    nums = report.split(" ")
    nums = numpy.array([int(i) for i in nums])
    if check_report(nums):
        safe_reports_1 += 1

    # Just brute force it for part 2
    safe_dampened = False
    for i, level in enumerate(nums): 
        new_nums = numpy.delete(nums, i)
        safe_dampened = check_report(new_nums)
        if safe_dampened:
            safe_reports_2 += 1
            break
        
print(f"Part 1 answer: {safe_reports_1}")
print(f"Part 2 answer: {safe_reports_2}")