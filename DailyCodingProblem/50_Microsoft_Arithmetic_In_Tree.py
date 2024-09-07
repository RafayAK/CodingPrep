"""
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""


class node:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


def recursive_tree_calculations(root):

    # leaf node
    if not root.left and not root.right:
        return root.data

    if root.data == '+':
        return recursive_tree_calculations(root.left) + recursive_tree_calculations(root.right)
    elif root.data == '-':
        return recursive_tree_calculations(root.left) - recursive_tree_calculations(root.right)
    elif root.data == '*':
        return recursive_tree_calculations(root.left) * recursive_tree_calculations(root.right)
    elif root.data == '/':
        return recursive_tree_calculations(root.left) / recursive_tree_calculations(root.right)


def simple_recursive_tree_calculations(root):

    # leaf node
    # if not root.left and not root.right:
    #     return root.data

    if str(root.data).isnumeric():
        return root.data

    return eval("{} {} {}".format(simple_recursive_tree_calculations(root.left),
                                  root.data,
                                  simple_recursive_tree_calculations(root.right)))

if __name__ == '__main__':
    tree = node(data='*',
                left=node('+', left=node(3), right=node(2)),
                right=node('+', left=node(4), right=node(5)))

    print(simple_recursive_tree_calculations(tree))
