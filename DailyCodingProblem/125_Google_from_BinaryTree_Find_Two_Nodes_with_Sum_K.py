"""
This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""

class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def two_nodes(root, s):
    compliment_dict = {}
    res = None
    def helper(root):
        nonlocal compliment_dict
        nonlocal res
        if root.val in compliment_dict:
            return root.val, compliment_dict[root.val]

        compliment_dict[s-root.val] = root.val

        if root.left:
            res = helper(root.left)

        if res:
            return res

        if root.right:
            res = helper(root.right)

        if res:
            return res

        return None

    res = helper(root)

    return None if res is None else res



if __name__ == '__main__':
    tree = node(10, left=node(5),
                right=node(15, left=node(11), right=node(15)))

    print(two_nodes(tree, 20))
    print(two_nodes(tree, 21))
    print(two_nodes(tree, 23))