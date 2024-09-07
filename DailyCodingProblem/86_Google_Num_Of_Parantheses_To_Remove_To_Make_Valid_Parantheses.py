"""
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses
to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def insert(self, data):
        self.stack.insert(0, data)

    def pop(self):
        top = self.stack[0]
        del self.stack[0]
        return top

    def peak(self):
        return self.stack[0] if len(self.stack)>0 else None

    def __str__(self):
        return "{}".format(self.stack)


def parentheses_to_remove(s):
    parentheses_stack = Stack()

    parentheses_stack.insert(s[0])

    for p in s[1:]:
        if parentheses_stack.peak() == '(' and p == ')':
            parentheses_stack.pop()
        else:
            parentheses_stack.insert(p)

    return parentheses_stack.__len__()


if __name__ == '__main__':
    print(parentheses_to_remove("()())()"))  # 1
    print(parentheses_to_remove(")("))  # 2
    print(parentheses_to_remove("()(((")) # 3
    print(parentheses_to_remove(")()((("))  # 4
