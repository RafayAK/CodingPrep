"""
This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.

"""

class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)
        

def level_with_min_sum(root):
    level_sums = []
    def helper(root, level=0):
        nonlocal level_sums
        try:
            level_sums[level]+=root.data
        except:
            level_sums.append(root.data)
        
        if root.left:
            helper(root.left, level+1)
        
        if root.right:
            helper(root.right, level+1)

    helper(root)
    return level_sums.index(min(level_sums))

if __name__ == '__main__':
    """
                           1          => 1, level=0
                          / \
                         2   3        => 5, level=1
                            / \
                           4   5      => 9, level=2
       """

    tree = node(1, left=node(2),
                right=node(3, left=node(4), right=node(5)))
    
    print(level_with_min_sum(tree))
    