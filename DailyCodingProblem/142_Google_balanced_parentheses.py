"""
This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can
represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""

# ord("(") = 40
# ord(")") = 41
# ord("*") = 42


def is_balanced(string, stack=[]):
    if len(string) == 0 and len(stack) == 0:
        return True

    if string:
        if string[0] == "(":
            return is_balanced(string[1:], stack + [string[0]])
        elif string[0] == ")":
            if stack and stack[-1] == "(":
                return is_balanced(string[1:], stack[:-1])
            else:
                return is_balanced(string[1:], stack + [string[0]])
        elif string[0] == "*":

            return is_balanced("("+string[1:], stack) or \
                   is_balanced(")"+string[1:], stack) or\
                   is_balanced(string[1:], stack)

    return False


if __name__ == '__main__':
    assert is_balanced("(()*") is True
    assert is_balanced("(*)") is True
    assert is_balanced(")*(") is False
