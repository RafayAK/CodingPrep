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

# Solution:
# 1 - A positive integer contains only digits
# 2 - A negative integer starts with '-' and the rest are positive integers
# 3 - A positive decimal contains one "." and the substrings before and after '.'
#     are positive
# 4 - A negative decimal starts with '-' and rest is positive decimal
# 5 - A positive number can be either a positive integer or decimal
# 6 - A negative number can be either a negative integer or decimal
# 7 - A scientific number can be contains one 'e' and the substring before and after e'
#     are either a positive or a negative number
# 8 - Finally, a number can be either a positive number, a negative number or a scientific number


def is_num_redux(string:str):
    return is_positive_number(string) or is_negative_number(string) or is_scientific_number(string)


def is_scientific_number(s:str):
    if s.count('e') != 1:
        return False

    before_e, after_e = s.split('e')

    return (is_positive_number(before_e) or is_negative_number(before_e)) and \
           (is_positive_number(after_e) or is_negative_number(after_e))


def is_positive_number(s:str):
    return is_positive_int(s) or is_positive_real(s)


def is_negative_number(s:str):
    return is_negative_int(s) or is_negative_real(s)


def is_negative_real(s:str):
    return s.startswith('-') and is_positive_real(s[1:])


def is_positive_real(s:str):
    if s.count('.') != 1:
        return False

    integer_part, decimal_part = s.split(".")

    return is_positive_number(integer_part) and is_positive_number(decimal_part)


def is_negative_int(s:str):
    return s.startswith('-') and is_positive_int(s[1:])


def is_positive_int(s:str):
    return s.isdigit()


if __name__ == '__main__':


    print(is_num_redux("10"))
    print(is_num_redux("-10"))
    print(is_num_redux("10.1"))
    print(is_num_redux("-10.1"))
    print(is_num_redux("1e5"))
    print(is_num_redux("1e-5"))
    print(is_num_redux("1e-5.2"))
    print()
    print(is_num_redux("a"))
    print(is_num_redux("x 1"))
    print(is_num_redux("a -2"))
    print(is_num_redux("-"))



