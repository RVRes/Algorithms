# https://realpython.com/python-gil/

# CPU bound task example. We see an increase in execution time in comparison to a scenario
# where it was written to be entirely single-threaded.
# This increase is the result of acquire and release overheads added by the lock.


import time
from threading import Thread
from multiprocessing import Pool

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


# single_threaded.py
start = time.time()
countdown(COUNT)
end = time.time()
print('Singe-thread time taken in seconds -', end - start)


# multi_threaded.py
t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('Multi-thread (2) time taken in seconds -', end - start)

# multi_processed.py -2
pool = Pool(processes=2)
start = time.time()
r1 = pool.apply_async(countdown, [COUNT // 2])
r2 = pool.apply_async(countdown, [COUNT // 2])
pool.close()
pool.join()
end = time.time()
print('Multi-process (2) Time taken in seconds -', end - start)

# multi_processed.py -4
pool = Pool(processes=4)
start = time.time()
r1 = pool.apply_async(countdown, [COUNT // 4])
r2 = pool.apply_async(countdown, [COUNT // 4])
r3 = pool.apply_async(countdown, [COUNT // 4])
r4 = pool.apply_async(countdown, [COUNT // 4])
pool.close()
pool.join()
end = time.time()
print('Multi-process (4) Time taken in seconds -', end - start)
