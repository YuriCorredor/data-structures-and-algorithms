from operator import length_hint
from timeit import default_timer as timer

def evaluate_tests(func, tests):
    total_passed = 0
    for test in tests:
        start = timer()
        output = func(**test['input'])
        end = timer()
        time_elapsed = end - start
        passed = output == test['output']
        if passed: total_passed += 1
        print(f'Expected output: {test["output"]}')
        print(f'Actual output: {output}')
        print(f'Time elapsed: {time_elapsed}')
        print(f'Passed: {passed} \n\n')
    print(f'TOTAL: {len(tests)}, PASSED: {total_passed}, FAILED: {len(tests) - total_passed} \n\n\n\n')