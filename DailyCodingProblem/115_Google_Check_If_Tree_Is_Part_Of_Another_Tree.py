"""
This problem was asked by Google.

Given two non-empty binary trees s and t, check whether tree t has exactly
the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
"""

class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}".format(self.data)

def check_if_tree_in_traget_tree(tree, target_tree):
    def helper(root):
        right_pattern = ""
        left_pattern = ""

        if root.left:
            left_pattern = helper(root.left)

        if root.right:
            right_pattern = helper(root.right)

        return str(root.data) + left_pattern + right_pattern

    pattern = helper(tree)
    target_pattern= helper(target_tree)

    return pattern in target_pattern


if __name__ == '__main__':
    """
       1
      / \
     2   3
        / \
       4   5
    """
    tree = node(1, left=node(2),
                right=node(3, left=node(4)))

    target_tree = node(1, left=node(2),
                right=node(3, left=node(4), right=node(5)))

    print(check_if_tree_in_traget_tree(tree, target_tree))
