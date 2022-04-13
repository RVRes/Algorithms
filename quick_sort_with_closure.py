from typing import List


def print_difference():
    previous_value = []

    def inner(value: List[int]):
        nonlocal previous_value
        if not previous_value:
            previous_value = value
            return
        red = '\033[31m'
        white = '\033[0m'
        green = '\033[32m'
        text_spacing: int = max(map(lambda x: len(str(x)), previous_value))
        interval_start = min(map(previous_value.index, value))
        new_value = previous_value[:interval_start] + value + previous_value[interval_start + len(value):]
        for i in previous_value:
            print(f'{red if i in value else white}{i:{text_spacing}}', end=' ')
        print()
        for pos, i in enumerate(new_value):
            print(f'{green if previous_value[pos] != new_value[pos] else white}{i:{text_spacing}}', end=' ')
        print(white)
        previous_value = new_value

    return inner


def _quick_sort(render, input_list: List[int]) -> List[int]:
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[len(input_list) // 2]
    left = [item for item in input_list if item < pivot]
    center = [pivot] * input_list.count(pivot)
    right = [item for item in input_list if item > pivot]
    render([*left, *center, *right])
    return _quick_sort(render, left) + center + _quick_sort(render, right)


def quick_sort(input_list: List[int]) -> List[int]:
    render = print_difference()
    return _quick_sort(render, input_list)


tests = [
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [1, 2, 3, 4, 5],
    [],
    [1, 1],
    [3, 10, -1, 3, 2, 7, 5, 0, -100]
]
for test in tests:
    print(f'{test} => {quick_sort(test)}')
    print()
