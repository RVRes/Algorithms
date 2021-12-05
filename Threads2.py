import threading
import time


# меняем локальную переменную из 2 потоков, работает
def test_thread_access_to_var():
    signal = False
    continue_thread = True

    def _thredfunc1():
        nonlocal continue_thread
        while continue_thread:
            time.sleep(1)
            nonlocal signal
            signal = True

    a = threading.Thread(target=_thredfunc1, args=())
    b = threading.Thread(target=_thredfunc1, args=())

    a.start()
    time.sleep(0.5)
    b.start()

    i = 10
    while i>0:
        if signal:
            print(time.strftime('%H:%M:%S', time.localtime()), '   Signal')
            signal = False
            i -=1

    continue_thread = False
    a.join()
    b.join()

    print(a.is_alive(), b.is_alive())

test_thread_access_to_var()
