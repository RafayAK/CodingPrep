"""
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}: ({}, {})".format(self.data,
                                     self.left.data if self.left else None,
                                     self.right.data if self.right else None)


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

def prune(root):
    def helper(node):

        can_rm_node, can_rm_left, can_rm_right = True, True, True
        if node.left:
            can_rm_left = helper(node.left)
            if can_rm_left:
                node.left = None
        if node.right:
            can_rm_right = helper(node.right)
            if can_rm_right:
                node.right = None

        if node.data == 1:
            can_rm_node = False

        return can_rm_node and can_rm_left and can_rm_right

    helper(root)
    return root

def prune_redux(root):
    if root is None:
        return None

    root.left, root.right = prune_redux(root.left), prune_redux(root.right)

    if root.left is None and root.right is None and root.data ==0:
        return None
    return root


if __name__ == '__main__':
    tree = Node(0,
                left=Node(1),
                right=Node(0,
                           left=Node(1, left=Node(0), right=Node(0)),
                           right=Node(0)))

    print(*print_level_wise(tree), sep='\n')
    tree = prune(root=tree)
    print("---"*3)
    print(*print_level_wise(tree), sep='\n')
    print("===" * 3)
    tree = Node(0,
                left=Node(1),
                right=Node(0,
                           left=Node(1, left=Node(0), right=Node(0)),
                           right=Node(0)))

    print(*print_level_wise(tree), sep='\n')
    tree = prune_redux(root=tree)
    print("---"*3)
    print(*print_level_wise(tree), sep='\n')

