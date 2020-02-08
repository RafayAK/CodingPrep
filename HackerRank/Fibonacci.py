
a,b = 1, 1
def fib_bottom_up(n):
    global a
    global b

    if n<2:
        return 1


    for i in range(2, n):
        c = a+b
        a = b
        b = c

    return b

def fib(n):
    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)



if __name__ == '__main__':
    # print(fib(1))
    # print(fib(2))
    # print(fib(3))
    # print(fib(4))
    # print(fib(5))
    # print(fib(6))
    # print(fib(7))
    # print(fib(8))
    # print(fib(9))
    # print(fib(10))
    # print(fib(50))
    print(fib_bottom_up(1))
    print(fib_bottom_up(2))
    print(fib_bottom_up(3))
    print(fib_bottom_up(1000))








