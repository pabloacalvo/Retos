from threading import Thread
from multiprocessing import Process
import time

def fibonnaci(number):
    if number == 1:
        return 0
    if number ==2:
        return 1
    
    return fibonnaci(number-1) + fibonnaci(number-2)


def show_fibonnaci_info(number):
    print(fibonnaci(number))

if __name__ == "__main__":
    start = time.sta

    thread1 = Process(target=show_fibonnaci_info, args=(42,))
    thread2 = Process(target=show_fibonnaci_info, args=(42,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()