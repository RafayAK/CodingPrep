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

        if right_value and left_value:
            max_sum = max(max_sum, left_value+right_value+root.value)
            return max(left_value+root.value, right_value+root.value, root.value)
        elif left_value:
            max_sum = max(max_sum, left_value + root.value)
            return max(left_value+root.value, root.value)
        elif right_value:
            max_sum = max(max_sum, right_value + root.value)
            return max(right_value + root.value, root.value)

        return root.value  # if leaf
    helper(root)
    return max_sum


if __name__ == '__main__':
    """
       1
      / \    max = 6
     2   3
    """
    tree_1 = Node(1, left=Node(2), right=Node(3))

    print(find_max_path_sum(tree_1))

    print("\n-------------\n")

    """
      -10
       / \       max=42   20
      9  20              /  \ 
        /  \            15   7
       15   7
    """
    tree_2 = Node(-10,
                  left=Node(9),
                  right=Node(20,
                             left=Node(15),
                             right=Node(7)))
    print(find_max_path_sum(tree_2))

    print("\n-------------\n")
    """
                                -15                                     6
                             /      \                                   / \               
                            5        6                                 3   9                                              
                          /  \       / \                                    \                                                                      
                        -8    1     3   9            max = 27                0                                 
                       /  \             \                                     \                                                           
                      2    6             0                                    -1                                                                 
                                        /  \                                 /                                                          
                                       4    -1                             10                                              
                                            /                                                                                   
                                           10                                                                                       
    """

    tree_3 = Node(-15,
                  left=Node(5,
                            left=Node(-8, left=Node(2), right=Node(6)),
                            right=Node(1)
                  ),
                  right=Node(6,
                             left=Node(3),
                             right=Node(9,
                                        right=Node(0, left=Node(4),
                                                   right=Node(-1, left=Node(10)))))
                             )

    print(find_max_path_sum(tree_3))

    print("\n-------------\n")

    """
          -10
           / \       max=42   20
          9  20              /  \ 
            /  \            15   7
           15   7
           /     \
        -15       -7
        """
    tree_4 = Node(-10,
                  left=Node(9),
                  right=Node(20,
                             left=Node(15, left=Node(-15)),
                             right=Node(7, right=Node(-7))))
    print(find_max_path_sum(tree_4))

