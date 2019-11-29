"""
This problem was asked by Google.

Given a binary tree of integers, find the maximum path sum between two nodes.
The path must go through at least one node, and does not need to go through the root.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        if self.right is not None:
            fmt = '{}({value!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({value!r}, {left!r})'
        else:
            fmt = '{}({value!r})'
        return fmt.format(type(self).__name__, **vars(self))


def find_max_path_sum(root : Node):
    max_sum = float('-inf')

    def helper(root):
        nonlocal max_sum
        left_value, right_value = None, None
        if root.left:
            left_value = helper(root.left)

        if root.right:
            right_value = helper(root.right)

        if left_value and right_value:
            max_sum = max(max_sum, root.value+left_value, root.value+right_value,
                      root.value+right_value+left_value)
        elif left_value:
            max_sum = max(max_sum, root.value + left_value)
        else:
            max_sum = max(max_sum, root.value + right_value)

        return root.value

    helper(root)
    return max_sum
