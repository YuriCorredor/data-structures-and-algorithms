from tests import tests
from evaluate_tests import evaluate_tests

def brute_force(nums):
    if len(nums) <= 1:
        return -1
    previous_num = nums[0]
    for index, num in enumerate(nums):
        if previous_num > num:
            return index
        previous_num = num
    return 0

evaluate_tests(brute_force, tests)

def binary_search(lowest_index, highest_index, condition):
    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        result = condition(middle_index, highest_index, lowest_index)
        if result == 'found': return middle_index
        elif result == 'left': highest_index = middle_index - 1
        else: lowest_index = middle_index + 1
    return 0

def solve(nums):
    if len(nums) <= 1:
        return -1

    lowest_index = 0
    highest_index = len(nums) - 1

    def condition(middle_index, highest_index, lowest_index):
        middle_number = nums[middle_index]
        if middle_number < nums[middle_index - 1]: return 'found'
        elif middle_number < nums[highest_index]: return 'left'
        else: return 'right'

    return binary_search(lowest_index, highest_index, condition)

evaluate_tests(solve, tests)