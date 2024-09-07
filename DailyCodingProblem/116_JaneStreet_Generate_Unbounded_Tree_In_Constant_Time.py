"""

This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.

"""

import random

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self._right = None
        self._left = None

        self.is_left_computed= False
        self.is_right_computed=False

    def __repr__(self):
        return str(self.data)

    @property
    def left(self):
        if self.is_left_computed:
            return self._left
        self._left = Node(random.randint(1, 10000))
        self.is_left_computed=True
        return self._left

    @property
    def right(self):
        if self.is_right_computed:
            return self._right
        self._right = Node(random.randint(1, 10000))
        self.is_right_computed=True
        return self._right


def generate():
    return Node(random.randint(1,10000))


def tree_breadthwise_traversal(head):
    nodes = []
    queue = []

    queue.append(head)

    while len(nodes) !=5:
        # take node from queue
        n = queue.pop(0)
        # add n's children to the queue
        queue.append(n.left)
        queue.append(n.right)

        nodes.append(n.data)

    return nodes



if __name__ == "__main__":
    tree_size = 5

    assert tree_size == len(tree_breadthwise_traversal(generate()))