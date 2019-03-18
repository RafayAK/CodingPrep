'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

import time
from threading import Thread

def scheduler():
    '''
    Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
    Example:

    >>> scheduler()
    Thread, you there?
    Hello, from thread
    Hello to you, too
    '''
    def delayed_execution(func, delay):
        time.sleep(delay)
        return func()

    def hello(name):
        print("Hello, " + name)


    job = Thread(target=delayed_execution, args=(lambda : hello('from thread'),2))
    job.start()

    print("Thread, you there?")
    time.sleep(3)
    print("Hello to you, too")


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)