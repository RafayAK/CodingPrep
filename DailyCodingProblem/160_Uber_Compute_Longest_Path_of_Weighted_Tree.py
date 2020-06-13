"""
This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1,
the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.
"""

# use adjacency matrix to solve this
#       a   b   c   d   e   f   g   h
#    ----------------------------------
#  a |  -   3   5   8   -   -   -   -
#  b |  3   -   -   -   -   -   -   -
#  c |  5   -   -   -   -   -   -   -
#  d |  8   -   -   -   2   4   -   -
#  e |  -   -   -   2   -   -   1   1
#  f |  -   -   -   4   -   -   -   -
#  g |  -   -   -   -   1   -   -   -
#  h |  -   -   -   -   1   -   -   -
#
# Start with a row(node) and find the longest path through that node and save it
# build all other paths by building on other paths
#

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def __repr__(self):
        return "{}->{}".format(self.val, self.children)



def longest_path(root):
    height, path = longest_height_and_path(root)
    return path

def longest_height_and_path(root):
    longest_path_so_far = float("-inf")
    highest, second_highest = 0, 0

    for length, child in root.children:
        height, longest_path_length = longest_height_and_path(child)

        longest_path_so_far = max(longest_path_so_far, longest_path_length)

        if height + length > highest:
            highest, second_highest = height + length, highest
        elif height + length > second_highest:
            second_highest = height + length

    return highest, max(longest_path_so_far, highest + second_highest)

if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    e.children = [(1, g), (1, h)]
    d.children = [(2, e), (4, f)]
    a.children = [(3, b), (5, c), (8, d)]


    print(a)

    print(longest_path(a))



# # Multi-Child Weighted Tree
# class Node:
#     def __init__(self, val, children : list = None, weights : list = None):
#         self.node = val
#         self.children = children
#         self.weights = weights
#
#     def __repr__(self):
#         return "{}->({}, {})".format(self.node, self.children, self.weights)
#
#
#
#
#
# def longest_path(tree):
#     # create adjacency mat
#     pass
#
#
# if __name__ == '__main__':
#     tree = Node(val='a', children=[Node('b'),
#                                    Node('c'),
#                                    Node('d', children=[Node('e', children=[Node('g'), Node('h')], weights=[1, 1]),
#                                                        Node('f')], weights=[2, 4])
#                                    ], weights=[3, 5, 8])
#
#     print(tree)