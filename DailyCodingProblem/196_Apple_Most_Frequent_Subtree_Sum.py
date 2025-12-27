"""
This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum.
The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.


"""

from collections import defaultdict

class Node:
    def __init__(self, data, left=None, right=None):
        self.data: int = data
        self.left: Node | None = left
        self.right: Node | None = right

    def is_leaf(self)->bool:
        if self.left is None and self.right is None:
            return True
        return False


    def __repr__(self):

        if self.right:
            fmt = f'{type(self).__name__}({self.data!r}, {self.left!r}, {self.right!r})'
        elif self.left:
            fmt = f'{type(self).__name__}({self.data!r}, {self.left!r})'
        else:
            fmt = f'{type(self).__name__}({self.data!r})'

        # print(vars(self))
        return fmt




def most_frequent_subtree_sum(node:Node):
    sum_freq = defaultdict(int)  # store sum:count

    def post_order_sum(n:Node):

        if n is None:
            return 0

        node_sum = post_order_sum(n.left) + post_order_sum(n.right) + n.data

        sum_freq[node_sum] +=1

        return node_sum


    post_order_sum(node)
    print(sum_freq)
    # print(f"Most frequent subtree sum: {max(sum_freq, key=sum_freq.get)}")

    return max(sum_freq, key=sum_freq.get)







if __name__ == '__main__':

    root: Node = Node(
        data=5,
        left=Node(2),
        right=Node(-5)
    )

    result = most_frequent_subtree_sum(root)
    assert result == 2
    print(f"Most frequent subtree sum: {result}")

    root_2: Node = Node(
        data=5,
        left=Node(2, left=Node(5), right=Node(3)),
        right=Node(-5, left=Node(5), right=Node(3))
    )

    result = most_frequent_subtree_sum(root_2)
    assert result == 3
    print(f"Most frequent subtree sum: {result}")

    root_3: Node = Node(
        data=1,
        left=Node(2, left=Node(3)),
    )

    result = most_frequent_subtree_sum(root_3)
    assert result == 3  # kinda random as all node sums will have the same frequency, depends on insertion order
    print(f"Most frequent subtree sum: {result}")