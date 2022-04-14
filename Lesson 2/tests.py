tests = []

tests.append({
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
})

# A list of size 8 rotated 5 times.
tests.append({
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
})

tests.append({
    'input': {
        'nums': [4, 5, 6, 1, 2, 3]
    },
    'output': 3
})

# A list that wasn't rotated at all.
tests.append({
    'input': {
        'nums': [1, 2, 3, 4, 5, 6]
    },
    'output': 0
})

# A list that was rotated just once.
tests.append({
    'input': {
        'nums': [5, 1, 2, 3, 4]
    },
    'output': 1
})

# A list that was rotated n-1 times, where n is the size of the list.
tests.append({
    'input': {
        'nums': [2, 3, 4, 5, 1]
    },
    'output': 4
})

# A list that was rotated n times, where n is the size of the list
tests.append({
    'input': {
        'nums': [1, 2, 6, 7, 8, 9, 12]
    },
    'output': 0
})

# An empty list.
tests.append({
    'input': {
        'nums': []
    },
    'output': -1
})

# A list containing just one element.
tests.append({
    'input': {
        'nums': [1]
    },
    'output': -1
})