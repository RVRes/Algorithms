import threading
from Logger import time_of_function


def writerA(x, event_for_wait, event_for_set):
    for i in range(10):
        event_for_wait.wait()  # wait for event
        event_for_wait.clear()  # clean event for future
        print(x)
        event_for_set.set()  # set event for neighbor thread


def init():
    # init events
    e1 = threading.Event()
    e2 = threading.Event()
    e3 = threading.Event()

    # init threads
    t1 = threading.Thread(target=writerA, args=(0, e1, e2))
    t2 = threading.Thread(target=writerA, args=(1, e2, e3))
    t3 = threading.Thread(target=writerA, args=(2, e3, e1))

    # start threads
    t1.start()
    t2.start()
    t3.start()

    e1.set()  # initiate the first event

    # join threads to the main thread
    t1.join()
    t2.join()
    t3.join()

# Миллион строк в файл в 1 потоке 1.203 секунды на ноуте
@time_of_function
def write_million_str_in_file():
    with open('test1.txt', 'w') as fout:
        for i in range(10000000):
            fout.write('1\n')


# Миллион строк в файл в 2 потока
@time_of_function
def write_million_str_in_file_threads():
    def writerB(filename, n):
        with open(filename, 'w') as fout:
            for i in range(n):
                fout.write('1\n')
        print(filename)

    t0 = threading.Thread(target=writerB, args=('test0.txt', 1000000,))
    t1 = threading.Thread(target=writerB, args=('test1.txt', 1000000,))
    t2 = threading.Thread(target=writerB, args=('test2.txt', 1000000,))
    t3 = threading.Thread(target=writerB, args=('test3.txt', 1000000,))
    t4 = threading.Thread(target=writerB, args=('test4.txt', 1000000,))
    t5 = threading.Thread(target=writerB, args=('test5.txt', 1000000,))
    t6 = threading.Thread(target=writerB, args=('test6.txt', 1000000,))
    t7 = threading.Thread(target=writerB, args=('test7.txt', 1000000,))
    t8 = threading.Thread(target=writerB, args=('test8.txt', 1000000,))
    t9 = threading.Thread(target=writerB, args=('test9.txt', 1000000,))

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()



