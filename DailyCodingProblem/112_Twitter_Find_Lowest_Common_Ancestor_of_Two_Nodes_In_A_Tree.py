"""
This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia(https://en.wikipedia.org/wiki/Lowest_common_ancestor):
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T that
has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""

class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def add_node(self, node):
        if node.data <= self.data:
            self.left = node
        else:
            self.right = node

        node.parent = self

    def __repr__(self):
        return "{}".format(self.data)

def find_lowest_common_ancestor(node_a, node_b):
    path_a = []
    path_b = []
    def helper(node, path= []):
        if node.parent:
            return helper(node.parent, [node.data]+path)

        return [node.data]+path

    # calculate paths for both
    path_a = helper(node_a)
    path_b = helper(node_b)

    # common nodes
    common_node = [n for n in path_a if n in path_b]
    return common_node[-1] # the last common node is the LCA


# simpler method:
# observation the LCA is always between the two values
def find_lowest_common_ancestor_redux(root, node_a, node_b):
    if root.data < node_a.data and root.data < node_b.data:
        return find_lowest_common_ancestor_redux(root.right, node_a, node_b)

    if root.data > node_a.data and root.data > node_b.data:
        return find_lowest_common_ancestor_redux(root.left, node_a, node_b)

    return root.data


# LCA can also be thought of as finding the merge point of two linked-lists(since parent is provided)
# idea from solution to my HackerRank "Find Merge Points of Two Lists"
def find_lowest_common_ancestor_redux_redux(node_a, node_b):
    iter_1 = node_a
    iter_2 = node_b

    while iter_1 != iter_2:
        if iter_1.parent is None:
            iter_1 = node_b
        else:
            iter_1 = iter_1.parent

        if iter_2.parent is None:
            iter_2 = node_a
        else:
            iter_2 = iter_2.parent



    return iter_2.data


if __name__ == '__main__':
    """
                            5
                          /    \
                         4       9
                        /      /    \
                       3      6     13
                               \    / \
                                8  10  14
                               /
                              7 
    """

    a = Node(5)
    b = Node(4)
    c = Node(3)
    d = Node(9)
    e = Node(6)
    f = Node(8)
    g = Node(7)
    h = Node(13)
    i = Node(10)
    j = Node(14)

    a.add_node(b)
    b.add_node(c)

    a.add_node(d)
    d.add_node(e)
    e.add_node(f)
    f.add_node(g)

    d.add_node(h)
    h.add_node(i)
    h.add_node(j)

    print(find_lowest_common_ancestor(b, d))  # 5
    print(find_lowest_common_ancestor(a, b))  # 5
    print(find_lowest_common_ancestor(c, b))  # 4
    print(find_lowest_common_ancestor(g, e))  # 6


    print("\n\n")

    print(find_lowest_common_ancestor_redux(a,b, d))  # 5
    print(find_lowest_common_ancestor_redux(a,a, b))  # 5
    print(find_lowest_common_ancestor_redux(a,c, b))  # 4
    print(find_lowest_common_ancestor_redux(a,g, e))  # 6

    print("\n\n")

    print(find_lowest_common_ancestor_redux_redux(b, d))  # 5
    print(find_lowest_common_ancestor_redux_redux(a, b))  # 5
    print(find_lowest_common_ancestor_redux_redux(c, b))  # 4
    print(find_lowest_common_ancestor_redux_redux(g, e))  # 6