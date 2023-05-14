import time
import threading

# You can specify that thread is a daemon before start. Daemon means that it is
# a service thread. Service threads will immediately close whe main thread
# finishes, normal threads - won't.
# https://stepik.org/lesson/628335/step/1?unit=624215


def get_data(data):
    for _ in range(5):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()), ))
thr.daemon = True
thr.start()
print('finish')

# Normal thread example - main thread finished but thread-1 is still working.
#
# [Thread-1 (get_data)] - 1684037761.4238915
# finish
# [Thread-1 (get_data)] - 1684037761.4238915
# [Thread-1 (get_data)] - 1684037761.4238915
# [Thread-1 (get_data)] - 1684037761.4238915
# [Thread-1 (get_data)] - 1684037761.4238915

# output with thr.daemon = True in line 16:
# all threads stopped with main thread.
# [Thread-1 (get_data)] - 1684038119.7077808
# finish
