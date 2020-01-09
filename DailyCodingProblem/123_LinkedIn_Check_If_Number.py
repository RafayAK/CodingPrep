"""
This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

    - "10", a positive integer
    - "-10", a negative integer
    - "10.1", a positive real number
    - "-10.1", a negative real number
    - "1e5", a number in scientific notation


And here are examples of non-numbers:

    - "a"
    - "x 1"
    - "a -2"
    - "-"
"""

def is_num(string):
    a = 0
    try:
        a = float(string)
    except ValueError:
        return False

    return True

if __name__ == '__main__':
    print(is_num("10"))
    print(is_num("-10"))
    print(is_num("10.1"))
    print(is_num("-10.1"))
    print(is_num("1e5"))
    print(is_num("1e-5"))


    print("\n------")
    print(is_num("a"))
    print(is_num("x 1"))
    print(is_num("a -2"))
    print(is_num("-"))




