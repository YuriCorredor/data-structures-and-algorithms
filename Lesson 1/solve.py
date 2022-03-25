from tests import tests
from evaluate_tests import evaluate_tests

#Linear search. The time complexity of linear search is O(N) and its space complexity is O(1).
def brute_force(cards, query):
    if not cards: return -1
    for index, card in enumerate(cards):
        if card == query: return index
    return -1

evaluate_tests(brute_force, tests)

#Binary search. The time complexity O(log N). You can verify that the space complexity of binary search is O(1).
#This fact is often stated as: binary search runs in logarithmic time.
def binary_search(lowest_index, highest_index, condition):
    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        result = condition(middle_index)
        if result == 'found': return middle_index
        elif result == 'left': highest_index = middle_index - 1
        else: lowest_index = middle_index + 1
    return -1

def solve(cards, query):

    lowest_index = 0
    highest_index = len(cards) - 1

    def condition(middle_index):
        middle_number = cards[middle_index]
        if middle_number == query:
            if middle_index - 1 >= 0 and cards[middle_index-1] == query: return 'left'
            else: return 'found'
        elif middle_number < query: return 'left'
        else: return 'right'
    
    return binary_search(lowest_index, highest_index, condition)

evaluate_tests(solve, tests)