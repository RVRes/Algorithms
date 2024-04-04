import time

for i in range(1, 100):
    print('\rCompleted: {}%'.format(i), end='')
    time.sleep(1)
