from itertools import *

# https://docs.python.org/3/library/itertools.html#itertools.count

# infinite iterators:

# COUNT, commonly used with map and zip functions
count_ = count(10, 2.5)
print(f'{count_}: {[next(count_) for _ in range(10)]}')

# COMPRESS -  filters elements from data returning only those that have a corresponding element in selectors
print(f"compress('ABCDEF',[1,0,1,0,1,1]): {list(compress('ABCDEF', [1, 0, 1, 0, 1, 1]))}")

# CYCLE
cycle_ = cycle('ABCD')
print(f"cycle('ABCD'): {[next(cycle_) for _ in range(10)]}")

# DROPWHILE
dw_ = dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])
print(f"dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]): {list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))}")


A = [3, 10, 12, 17]
print(f'permutations({A}): {list(permutations(A))}')
print(f'combinations({A}): {list(combinations(A, r=2))}')
