"""
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""
from inspect import getargspec
from itertools import dropwhile

class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # def __repr__(self):
    #     return "{}->({}, {})".format(self.data, self.left, self.right)

    #https: // codereview.stackexchange.com / a / 109410
    def __repr__(self):
        if self.right is not None:
            fmt = '{}({data!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({data!r}, {left!r})'
        else:
            fmt = '{}({data!r})'
        return fmt.format(type(self).__name__, **vars(self))


def invert_bst(root: node):

    root.left, root.right = root.right, root.left

    if root.left:
        invert_bst(root.left)

    if root.right:
        invert_bst(root.right)

    return root



if __name__=="__main__":
    bst = node('a',
               left=node('b',
                         left=node('d'),
                         right=node('e')),
               right=node('c',
                          left=node('f')))

    print(bst)

    inverted_bst = invert_bst(bst)

    print(inverted_bst)