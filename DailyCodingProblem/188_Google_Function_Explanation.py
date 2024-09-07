"""
This problem was asked by Google.

What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
How can we make it print out what we apparently want?
"""

# the print_i function is enclosed within the for loop where and is not evaluated until after make_functions
# when its finally evaluated the variable i which is global to print_i has mutated to 3, the last value in the list
# so it will print 3 in current state

# to fix this enclose print_i with another function that actually takes an attribute to define the signature of the
# function resulting in def make_print(1), def make_print(2) and def make_print(3), all separate calls to print_i.

# https://eev.ee/blog/2011/04/24/gotcha-python-scoping-closures/

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def make_print(i):
            def print_i():
                print(i)
            return print_i
        flist.append(make_print(i))
    return flist


functions = make_functions()
for f in functions:
    f()