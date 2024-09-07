'''
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function
should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.

'''

memo_table = {} # store what strings are True or False

def check_regular(reg_exp, string):

    if (reg_exp, string) in memo_table: # return if in memo_table
        return memo_table[(reg_exp, string)]

    if len(reg_exp)==0 and len(string)==0: # both stings empty
        memo_table[(reg_exp, string)] = True
        return memo_table[(reg_exp, string)]

    # string is empty but a 'char*...' like reg expression is left, see if we can end it
    if len(reg_exp) > 1 and reg_exp[1] == '*' and len(string)==0:
        memo_table[(reg_exp, string)] = check_regular(reg_exp[2:], string)
        return memo_table[(reg_exp, string)]

    if len(reg_exp)==0 and len(string)!=0: # string is still remaining
        memo_table[(reg_exp, string)] = False
        return memo_table[(reg_exp, string)]
    if len(reg_exp)!=0 and len(string)==0: # reg_exp is still remaining
        memo_table[(reg_exp, string)] = False
        return memo_table[(reg_exp, string)]

    # matched the first char, store result it as bool
    first_char_match = True if reg_exp[0] == string[0] or reg_exp[0] == '.' else False

    if len(reg_exp) > 1 and reg_exp[1] == '*':
        if first_char_match: # if True, check by matching or ignoring the 'char*'
            memo_table[(reg_exp, string)] = check_regular(reg_exp[2:], string) or check_regular(reg_exp, string[1:])
        else:
            # ignore the 'char*', it didn't match
            memo_table[(reg_exp, string)] = check_regular(reg_exp[2:], string)
    elif first_char_match:
        # got a match
        memo_table[(reg_exp, string)] = check_regular(reg_exp[1:], string[1:])
    else:
        # got no match
        memo_table[(reg_exp, string)] = False

    return memo_table[(reg_exp, string)]

if __name__ == '__main__':
    # "aab"
    # "c*a*b"
    #
    reg_exp = ".*"
    string = "aab"

    print(check_regular(reg_exp,string))