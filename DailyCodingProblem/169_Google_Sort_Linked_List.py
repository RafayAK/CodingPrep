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

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self, l:list):
        if self.head is None:
            self.head = Node(data=l[0])
            l = l[1:]

        curr_node = self.head
        while l:
            curr_node.nxt = Node(data=l[0])
            curr_node = curr_node.nxt
            l = l[1:]

    # unoptimized bubble sort O(N^2) constant space
    def sort_ll_bubble(self):
        made_swap = True

        while made_swap:
            curr_node = self.head
            next_node = curr_node.nxt
            made_swap = False

            while next_node:
                if curr_node.data > next_node.data:
                    curr_node.data, next_node.data = next_node.data, curr_node.data
                    made_swap = True
                curr_node = next_node
                next_node = next_node.nxt


    def __repr__(self):
        return "H->{}".format(self.head)







if __name__ == '__main__':
  ll = LinkedList()
  ll.create_linked_list([4, 1, -3, 99])
  print(ll)
  ll.sort_ll_bubble()
  print(ll)
