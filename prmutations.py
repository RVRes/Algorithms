from itertools import *

A = [3, 10, 12, 17]
for i in permutations(A):
    print(i, end=' ')  # abc acb bac bca cab cba
# print()

print('')
for i in combinations(A, 4):
    print(i, end=' ')  # abc acb bac bca cab cba
print()
