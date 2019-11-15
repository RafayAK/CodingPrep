"""
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must be less than or equal
to the root and the key in the right child must be greater than or equal to the root.

"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



# checks if tree is BST if inorder traversal is correct
def check_is_BST(root):

    def helper(root):
        inorder_status = True
        root_val = root.data

        if root.left and inorder_status:
            left_val, inorder_status = helper(root.left)

            if inorder_status is False or left_val > root_val:
                return root_val, False

        if root.right and inorder_status:
            right_val, inorder_status = helper(root.right)
            if inorder_status is False or right_val < root_val:
                return root_val, False

        return root_val, inorder_status

    return helper(root)[1]





if __name__ == '__main__':
    false_bst = Node(8,
                     left=Node(4,
                               left=Node(7),
                               right=Node(5)
                               ),
                     right=Node(10,
                                left=Node(9),
                                right=Node(11)
                                )
                     )

    print(check_is_BST(false_bst))  # false

    tree = Node(5,
                left=Node(2,
                          left=Node(1),
                          right=Node(4,
                                     left=Node(3))
                          ),
                right=Node(6,
                           right=Node(9,
                                      right=Node(12,
                                                 left=Node(11)))))

    print(check_is_BST(tree))  # True



