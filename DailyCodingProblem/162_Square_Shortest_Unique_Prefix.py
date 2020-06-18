"""
This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f
"""


# rough idea
#
#   1st iter     2nd iter    3rd iter
#
#     d             d           d
#     c             c           c
#     a             ap          app
#     a             ap          apr
#     f             f           f
#