"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""
class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def all_paths(root):
    paths = []
    def helper(root, path):
        nonlocal paths
        if root.left:
            helper(root.left, path+[root.data])

        if root.right:
            helper(root.right, path+[root.data])

        if root.left is None and root.right is None:
            paths.append(path+[root.data])

    helper(root, [])
    return paths

if __name__ == '__main__':
    tree = node(1, left=node(2),
                right=node(3, left=node(4), right=node(5)))

    print(all_paths(tree))