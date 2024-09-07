"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""


def shifted_but_equal(str_1, str_2):
    iter_2 = 0, None
    # find where in str_2 the first letter of str_1 is
    for i in range(len(str_2)):
        if str_2[i] == str_1[0]:
            iter_2 = i
            break

    if iter_2 is None:
        return False

    for j in range(len(str_1)):
        if str_1[j] != str_2[iter_2]:
            return False

        if iter_2 == len(str_2)-1:
            iter_2=0
        else:
            iter_2+=1
    return True

def shifted_but_equal_redux(str_1, str_2):
    return str_1 and str_2 and len(str_1) == len(str_2) and str_1 in str_2*2


if __name__ == '__main__':
    print(shifted_but_equal('abc', 'cab'))
    print(shifted_but_equal('abcde', 'cdeab'))
    print(shifted_but_equal('abc', 'acb'))

    print(shifted_but_equal_redux('abc', 'cab'))
    print(shifted_but_equal_redux('abcde', 'cdeab'))
    print(shifted_but_equal_redux('abc', 'acb'))


