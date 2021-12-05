import timeit

print(timeit.timeit('for i in range(100): pass', number=10000))
print(timeit.timeit('a = "1"', number=100000))