"""
This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # https: // codereview.stackexchange.com / a / 109410
    def __repr__(self):
        if self.right is not None:
            fmt = '{}({val!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({val!r}, {left!r})'
        else:
            fmt = '{}({val!r})'
        return fmt.format(type(self).__name__, **vars(self))


def get_postorder(root, output_arr=None):
    if output_arr is None:
        output_arr = []

    if root.left:
        output_arr = get_postorder(root.left, output_arr)
    if root.right:
        output_arr = get_postorder(root.right, output_arr)

    return output_arr + [root.val]


def make_tree_from_post_order(sequence):
    if len(sequence) == 0:
        return None

    root = Node(sequence[-1])

    if len(sequence) == 1:
        return root

    sequence = sequence[:-1]

    # find the index of the value that is greater than the root value.
    # Since this is a BST everything to the left of that index is the
    # left part of the original tree and everything on the right of index
    # is in the right part of the original tree.
    for index, val in enumerate(sequence):
        if val > root.val:
            root.left = make_tree_from_post_order(sequence[:index])
            root.right = make_tree_from_post_order(sequence[index:])
            break

    return root

if __name__ == '__main__':
    tree = Node(5,
                left=Node(3,
                          left=Node(2),
                          right=Node(4)),
                right=Node(7,
                           right=Node(8)))
    print(tree)
    recreated_tree = make_tree_from_post_order([2, 4, 3, 8, 7, 5])
    print(recreated_tree)

    assert get_postorder(tree) == get_postorder(recreated_tree)

    """
                            8
                           /  \
                          2    9
                         /  \
                       1    3
       """
    tree_1 = Node(8,
                  left=Node(2,
                            left=Node(1),
                            right=Node(3)),
                  right=Node(9)
                  )

    print(tree_1)
    recreated_tree = make_tree_from_post_order(get_postorder(tree_1))
    print(recreated_tree)
    assert get_postorder(tree_1) == get_postorder(recreated_tree)
