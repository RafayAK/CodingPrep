"""
This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


def naive_succsessor(root, target, prev=None):
    inorder = []
    def get_inorder_traveral(r):
        nonlocal inorder
        if r.left:
            get_inorder_traveral(r.left)

        inorder.append(r.data)

        if r.right:
            get_inorder_traveral(r.right)


    get_inorder_traveral(root)

    try:
        successor_index = inorder.index(target) +1
        return inorder[successor_index] if successor_index < len(inorder) else None
    except ValueError:
        return None


if __name__ == '__main__':
    root = Node(10, left=Node(5), right=Node(30, left=Node(22), right=Node(35)))
    print(naive_succsessor(root, 22))
    print(naive_succsessor(root, 5))
    print(naive_succsessor(root, 10))
    print(naive_succsessor(root, 35))
    print(naive_succsessor(root, 355))  # value error
