"""
This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt=nxt

    def __repr__(self):
        return "{}->{}".format(self.data, self.nxt)

# unoptimized bubble sort O(N^2) constant space
def sort_ll_bubble(head):
    next_node = head.nxt
    prev_node = head

    while prev_node and next_node:
        if prev_node.data > next_node.data:
            # swap
            prev_node.nxt = next_node.nxt
            next_node.nxt = prev_node



if __name__ == '__main__':
    ll = Node(4, nxt=Node(1, nxt=Node(-3, nxt=Node(99))))
    print(ll)
    sort_ll_bubble(ll)
    print(ll)
