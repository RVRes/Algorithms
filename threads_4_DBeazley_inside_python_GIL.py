# https://www.youtube.com/watch?v=ph374fJqFPE
# David Beazley presentation on the Python GIL, presented at the Chicago Python User's group meeting, June, 2009

# Testing sequential vs threading run CPU-bounded function

import time
from threading import Thread


def count(n):
    while n > 0:
        n -= 1


N = 100000000

# 2 run in sequence 1 by 1
start = time.time()
count(N)
count(N)
end = time.time()
print('sequential run time taken in seconds -', end - start)

# 2 run in threads (they also will run one by one)
start = time.time()
t1 = Thread(target=count, args=(N,))
t1.start()
t2 = Thread(target=count, args=(N,))
t2.start()
t1.join()
t2.join()
end = time.time()
print('Multi-thread (2) time taken in seconds -', end - start)


# sequential run time taken in seconds - 12.980352401733398
# Multi-thread (2) time taken in seconds - 18.84749722480774


# During I/O operations - global lock released, so it is possible to run another load in parallel.
# Only main thread handles signals - during periodic Check (100 ticks by default)
# Tick is loosely map to interpreter instructions.
# library dis can disassemble python code to byte code

# python does not have any control on thread scheduling (OS do), Ctrl+c - wont work - it starts switch tread every tick
# looks like obsolet - Ctrl+C works now

# to acquire GIL, check it's free, if not -go to sleep and wait for signal
# to release GIL, free it and signal
# signal goes to OS



