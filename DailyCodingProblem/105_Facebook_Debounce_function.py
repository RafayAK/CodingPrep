"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.
"""

# great visualization : http://demo.nimius.net/debounce_throttle/
# decorators : https://www.datacamp.com/community/tutorials/decorators-python
# source: https://jonlabelle.com/snippets/view/python/python-debounce-decorator-function

from threading import Timer


import time  # only for testing


def debounce(wait):
    """
    As long as the function is being called don't execute it
    after the function call has ended execute the function after N seconds.
    Args:
        wait (int): wait time
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            def call_it():
                func(*args, **kwargs)

            try:
                decorator.debounced_func.cancel()
            except AttributeError:
                pass
            decorator.debounced_func = Timer(wait, call_it)
            decorator.debounced_func.start()

        return wrapper

    return decorator


@debounce(1)
def print_symbol(symbol):
    print(symbol, end="")


if __name__ == '__main__':

    # so the star function will be called after its not being pinned anymore, it will use the latest call, no queuing
    # of calls
    for _ in range(20):
        print_symbol("*")
        print("-", end="")


    time.sleep(3)  # sleep for 2 secs before running the next loop
    print("\n")

    symbols = ['*', '%', '$']
    #                                             0 1 2 3 4 5 6 7 8
    # for range 5(i.e 0-4) it should print '%' -> * % $ * % $

    for i in range(5):
        print_symbol(symbols[i%3])



