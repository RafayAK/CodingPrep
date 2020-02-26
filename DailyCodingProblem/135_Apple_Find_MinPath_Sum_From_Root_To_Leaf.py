"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def get_min_path(root):
    min_sum = float('inf')
    min_path = []

    def helper(root, curr_path=[]):
        nonlocal min_path
        if root.left:
            helper(root.left, curr_path + [root.data])

        if root.right:
            helper(root.right, curr_path + [root.data])

        if root.left is None and root.right is None:
            if sum(curr_path) < min_sum:
                min_path = curr_path + [root.data]
                # print(min_path)

    helper(root)
    return min_path

if __name__ == '__main__':
    tree = Node(10,
                left=Node(5, right=Node(2)),
                right=Node(5,
                           right=Node(1, left=Node(-1))))

    print(get_min_path(tree))
