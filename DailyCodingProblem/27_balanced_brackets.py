'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''


bracket_vocab = {'(': 1,
                 ')': 2,
                 '[': 3,
                 ']': 4,
                 '{': 5,
                 '}': 6}

# The ord() method returns an integer representing Unicode code point for the given Unicode character.

def balanced(string):
    stack = []

    for i in string:
        if len(stack) ==0:
            stack.append(i)
        elif bracket_vocab[i]-1 == bracket_vocab[stack[-1]]:
            # found matching bracket
            stack.pop(-1)
        else:
            stack.append(i)

    if len(stack) ==0:
        # successfully matched all brackets
        return True
    else:
        return False


if __name__ == '__main__':
    # string = "([)]"
    string = "([])[]({})"
    # string = "((()"
    print(balanced(string))
