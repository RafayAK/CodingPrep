"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g

"""


class node:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


def inorder(root):
    list_of_nodes = []

    def recursive_helper(node):
        if node.left:
            recursive_helper(node.left)

        list_of_nodes.append(node.data)

        if node.right:
            recursive_helper(node.right)

    recursive_helper(root)
    return list_of_nodes

def preorder(root):
    list_of_nodes = []

    def recursive_helper(node):
        list_of_nodes.append(node.data)

        if node.left:
            recursive_helper(node.left)

        if node.right:
            recursive_helper(node.right)

    recursive_helper(root)
    return list_of_nodes


def postorder(root):
    list_of_nodes = []

    def recursive_helper(node):
        if node.left:
            recursive_helper(node.left)

        if node.right:
            recursive_helper(node.right)

        list_of_nodes.append(node.data)

    recursive_helper(root)
    return list_of_nodes


def make_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = node(preorder[0])

    if len(preorder) == 1:
        return root

    for i, char in enumerate(inorder):
        if preorder[0] == char:
            root.left = make_tree(preorder=preorder[1:i+1], inorder=inorder[:i])
            root.right= make_tree(preorder=preorder[i+1:], inorder=inorder[i+1:])

    return root


"""
tree_1:
    a
   / \
  b   c
 / \ / \
d  e f  g


tree_2:

            a
           / \
          b   c
         / \ / \
        d  e f  g
       / \     / \
      h   i   j   k
                   \
                    l
"""



if __name__ == '__main__':

    # create tree and then check against its post, pre and in order lists
    tree_1 = node('a',
                  left=node('b', left=node('d'), right=node('e')),
                  right=node('c', left=node('f'), right=node('g')))

    created_tree = make_tree(preorder=preorder(tree_1), inorder=inorder(tree_1))

    assert preorder(created_tree) == preorder(tree_1)
    assert inorder(created_tree) == inorder(tree_1)
    assert postorder(created_tree) == postorder(tree_1)

    tree_2 = node('a',
                  left=node('b',
                            left=node('d', left=node('h'), right=node('i')),
                            right=node('e')),
                  right=node('c',
                             left=node('f'),
                             right=node('g', left=node('j'), right=node(data='k', right=node('l'))))
                  )
    created_tree = make_tree(preorder=preorder(tree_2), inorder=inorder(tree_2))

    assert preorder(created_tree) == preorder(tree_2)
    assert inorder(created_tree) == inorder(tree_2)
    assert postorder(created_tree) == postorder(tree_2)