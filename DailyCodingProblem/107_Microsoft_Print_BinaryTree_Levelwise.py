"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""

class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def print_level_wise(root, l=0, nodes=None):
    if nodes is None:  # set default value
        nodes = []
    try:
        nodes[l].append(root.data)
    except:
        nodes.append([])
        nodes[l].append(root.data)

    if root.left:
        nodes = print_level_wise(root.left, l+1, nodes)

    if root.right:
        nodes = print_level_wise(root.right, l + 1, nodes)

    return nodes


# recommended solution
from queue import Queue
def print_level_wise_redux(root):
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        node = queue.get()
        if node.left:
            queue.put(node.left)

        if node.right:
            queue.put(node.right)
        print(node.data)


if __name__ == '__main__':
    tree = node(1, left=node(2),
                right=node(3, left=node(4), right=node(5)))
    print(*print_level_wise(tree), sep='\n')
    print("----")
    print_level_wise_redux(tree)