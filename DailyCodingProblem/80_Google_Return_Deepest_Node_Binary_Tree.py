"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def deepest_node(tree):

    def helper(root, depth=0):
        if root.left and root.right:
            return max(helper(root.left,depth+1), helper(root.right, depth+1), key=lambda x:x[1])
        elif root.left:
            return helper(root.left, depth+1)
        elif root.right:
            return helper(root.right, depth+1)

        return root.data, depth
    res = helper(tree)
    return res[0]


if __name__ == '__main__':
    tree = Node('a', left=Node('b', left=Node('d')), right=Node('c'))
    print(deepest_node(tree))  # e

    tree = Node('a', left=Node('b', left=Node('d')), right=Node('c', left=Node('e', left=Node('f'))))
    print(deepest_node(tree))  # f
