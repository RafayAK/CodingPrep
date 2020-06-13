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

# There are two case to take care of here:
#  1. either the longest path is a in a straight ward trajectory down from a node or
#  2. its a round trajectory where the path first goes up the nodes and then down i.e.
#     combo of two of the longest straight paths from a node
#
#  We keep track of the max_path_seen_so_far which can either be straight or a combo
#  and propagate it up the tree as we recursively look at each node
#

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def __repr__(self):
        return "{}->{}".format(self.val, self.children)

def get_longest_path(tree):
    _, longest_path_in_tree = get_longest_length_and_path(root=tree)
    return longest_path_in_tree

def get_longest_length_and_path(root):
    max_path_seen_so_far = float("-inf")
    longest, second_longest = 0, 0  # stores longest and and second longest straight paths from this root

    for length, child in root.children:

        # get the max longest path that goes through this child and
        # longest_straight_path that goes through this child
        longest_straight_path, max_path_length = get_longest_length_and_path(child)

        max_path_seen_so_far = max(max_path_seen_so_far, max_path_length)

        if longest_straight_path + length > longest:
            longest, second_longest = longest_straight_path + length, longest
        elif longest_straight_path + length > second_longest:
            second_longest = longest_straight_path + length

    return longest, max(max_path_seen_so_far, longest+second_longest)



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

    print(get_longest_path(a))
    print(get_longest_path(d))


