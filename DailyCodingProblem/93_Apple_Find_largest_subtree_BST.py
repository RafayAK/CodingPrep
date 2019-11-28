"""
This problem was asked by Apple.

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        if self.right is not None:
            fmt = '{}({data!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({data!r}, {left!r})'
        else:
            fmt = '{}({data!r})'
        return fmt.format(type(self).__name__, **vars(self))


def find_largest_bst_subtree(root):
    largest_root = None
    largest_size = 0

    def helper(root):
        nonlocal largest_root, largest_size
        is_bst = True
        size = 0
        if root.left:
            child_data, check_bst, temp_size = helper(root.left)
            is_bst = is_bst and child_data <= root.data and check_bst
            size += temp_size

        if root.right:
            child_data, check_bst, temp_size = helper(root.right)
            is_bst = is_bst and child_data > root.data and check_bst
            size += temp_size

        if is_bst and largest_size < size+1:
            largest_size = size+1
            largest_root = root

        return root.data, is_bst, size+1

    helper(root)
    return largest_root, largest_size


if __name__ == '__main__':
    """
                         5
                        /  \
    largest, size 3--> 2    4
                      /  \
                    1    3
    """

    tree_1 = Node(data=5,
                  left=Node(2,
                            left=Node(1),
                            right=Node(3)),
                  right=Node(4)
                  )

    largest_tree, size_of_largest_tree = find_largest_bst_subtree(tree_1)

    print("Size of largest tree : {}".format(size_of_largest_tree))
    print("Largest tree is : \n {}".format(largest_tree))

    # --------------------
    print("\n ----------- \n")

    """
           50
         /    \
      30       60  <----- largest, size 5
     /  \     /  \ 
    5   20   45    70
                  /  \
                65    80
    """

    tree_2 = Node(data=50,
                  left=Node(30,
                            left=Node(5),
                            right=Node(20)),
                  right=Node(60,
                             left=Node(45),
                             right=Node(70,
                                        left=Node(65),
                                        right=Node(80)))
                  )

    largest_tree, size_of_largest_tree = find_largest_bst_subtree(tree_2)

    print("Size of largest tree : {}".format(size_of_largest_tree))
    print("Largest tree is : \n {}".format(largest_tree))


    print("\n ----------- \n")

    """
            6 <----- largest, size 7
         /    \
        4       10  
       /  \     /  \ 
      3    5   9    11
              
    """

    tree_3 = Node(data=6,
                  left=Node(4,
                            left=Node(4),
                            right=Node(5)),
                  right=Node(10,
                             left=Node(9),
                             right=Node(11))
                  )

    largest_tree, size_of_largest_tree = find_largest_bst_subtree(tree_3)

    print("Size of largest tree : {}".format(size_of_largest_tree))
    print("Largest tree is : \n {}".format(largest_tree))