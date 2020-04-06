"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def nxt_of_nxt(self):
        if self.nxt:
            return self.nxt.nxt
        else:
            return None
    def __repr__(self):
        return "{}->{}".format(self.data, self.nxt)

def swap_every_two(ll):
    head = None
    i = None
    j = ll
    k = ll.nxt

    while j and k:
        j.nxt = k.nxt
        k.nxt = j
        if i:
            i.nxt = k
        if head is None:
            head = k

        j, k = k, j
        i = k
        j = j.nxt_of_nxt()
        k = k.nxt_of_nxt()

    return head


if __name__ == '__main__':
    print('\n ----- Test-1 -----\n')
    ll = Node(1, nxt=Node(2, nxt=Node(3, nxt=Node(4))))

    print("Original:", ll)
    ll = swap_every_two(ll)
    print("Swapped:", ll)

    print('\n ----- Test-2 -----\n')

    ll = Node(1, nxt=Node(2, nxt=Node(3)))
    print("Original:", ll)
    ll = swap_every_two(ll)
    print("Swapped:", ll)


    print('\n ----- Test-3 -----\n')

    ll = ll = Node(1, nxt=Node(2, nxt=Node(3, nxt=Node(4, nxt=Node(5)))))
    print("Original:", ll)
    ll = swap_every_two(ll)
    print("Swapped:", ll)