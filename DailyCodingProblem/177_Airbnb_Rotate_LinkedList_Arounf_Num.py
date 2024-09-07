'''
This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
'''

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def __repr__(self):
        return "{}->{}".format(self.data, self.nxt)


def rotate_list(head, k=0):
    def rotate_helper():
        nonlocal  head
        # find the first node, second_last node, and last node
        first, second_last, last = head, head, head
        while last.nxt:
            second_last = last
            last = last.nxt

        # rotate
        last.nxt = first
        second_last.nxt = None
        head = last


    for i in range(k):
        rotate_helper()


    return head


if __name__ == '__main__':
    l1 = Node(7, nxt=Node(7, nxt=Node(3, nxt=Node(5))))
    print(l1)
    l1 = rotate_list(l1, 2)
    print(l1)

    l2 = Node(1, nxt=Node(2, nxt=Node(3, nxt=Node(4, nxt=Node(5)))))
    print(l2)
    l2 = rotate_list(l2, 3)
    print(l2)

    l3 = Node(1)
    print(l3)
    l3 = rotate_list(l3, 3)
    print(l3)