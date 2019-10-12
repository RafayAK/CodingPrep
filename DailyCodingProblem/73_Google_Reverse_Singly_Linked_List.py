"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "{}->{}".format(self.data, self.next)

def reverse_ll(head):

    prev_node = None
    curr_node = head
    next_node = head.next

    while next_node:
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        next_node = curr_node.next

    curr_node.next = prev_node

    return curr_node

def print_ll(head):
    curr = head

    while curr:
        print(curr.data, end=' ')
        curr = curr.next

    print()

if __name__ == '__main__':

    # 1->2->3->4->5
    linked_list = Node(data=1, next=Node(data=2, next=Node(data=3, next=Node(data=4, next=Node(5)))))

    print("linked list before reversal:")
    # print_ll(linked_list)
    print(linked_list)

    print("linked list after reversal:")
    linked_list = reverse_ll(linked_list)
    # print_ll(linked_list)
    print(linked_list)