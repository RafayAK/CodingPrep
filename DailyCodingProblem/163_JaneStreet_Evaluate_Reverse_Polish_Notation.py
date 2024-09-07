"""
This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

# keep a window of 3, start from the left of the array and perform th operation
# when the 3rd element of the window contains an arithmetic op

def eval_reverse_polish(exp:list):
    start = 0
    end = start+2

    while isinstance(exp[end], (int, float, complex)) and not isinstance(exp[end], bool):
        start = start+1
        end = end+1

    op = exp[end]
    val = 0
    if op == "+":
        # add values
        val = exp[start] + exp[start+1]
    elif op == '-':
        # subtract vals
        val = exp[start] - exp[start+1]
    elif op == '/':
        # divide vals
        val = exp[start] / exp[start+1]
    elif op == '*':
        # multiply vals
        val = exp[start] * exp[start+1]
    else:
        raise Exception("Unknown arithmetic operation : {}".format(op))

    exp[start:end+1] = [val]

    if len(exp) == 1:
        return exp[0]
    else:
        return eval_reverse_polish(exp)

# better implementation
# solve it with stack
PLUS = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"

OPS = [PLUS, MINUS, MULTIPLY, DIVIDE]

def eval_reverse_polish_redux(exp:list):
    stack = []

    for symbol in exp:
        if symbol in OPS:
            # take out the most recent to values and apply the operation on them
            val2, val1 = stack.pop(-1), stack.pop(-1)
            if symbol == PLUS:
                stack.append(val1 + val2)
            elif symbol == MINUS:
                stack.append(val1 - val2)
            elif symbol == MULTIPLY:
                stack.append(val1 * val2)
            elif symbol == DIVIDE:
                stack.append(val1 / val2)
        else:
            # add to the top of the stack
            stack.append(symbol)

    return stack[0]

if __name__ == '__main__':
    print(eval_reverse_polish([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))

    print(eval_reverse_polish_redux([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))
