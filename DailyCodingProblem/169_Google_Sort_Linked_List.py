"""
This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""


class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def __repr__(self):
        return "{}->{}".format(self.data, self.nxt)


class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self, l: list):
        if self.head is None:
            self.head = Node(data=l[0])
            l = l[1:]

        curr_node = self.head
        while l:
            curr_node.nxt = Node(data=l[0])
            curr_node = curr_node.nxt
            l = l[1:]

    # unoptimized bubble sort O(N^2) constant space
    # changes data among nodes
    def sort_bubble_dataxchnage(self):
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

    # Slightly more optimized, only links being exchanged instead of data
    # still O(N^2) and constant time
    def sort_bubble_linkxchange(self):
        made_swap = True

        while made_swap:
            curr_node = self.head
            next_node = curr_node.nxt
            prev_node = None
            made_swap = False

            while next_node:
                if curr_node.data > next_node.data:
                    curr_node.nxt = next_node.nxt
                    next_node.nxt = curr_node
                    if prev_node is not None:
                        prev_node.nxt = next_node
                    else:
                        self.head = next_node

                    curr_node, next_node = next_node, curr_node
                    made_swap = True

                prev_node = curr_node
                curr_node = next_node
                next_node = next_node.nxt

    # Optimized solution, O(NlogN) and constant space
    def merge_sort(self):
        self.head = self.merge_sort_helper(self.head)

    @staticmethod
    def split_ll(head):
        slow = None
        fast = head
        while fast and fast.nxt:
            slow = head if slow is None else slow.nxt
            fast = fast.nxt.nxt

        mid = slow.nxt
        slow.nxt = None  # None the ptr so that head to this node becomes left
        return mid

    @staticmethod
    def merge_sort_helper(head):
        if head is None or head.nxt is None:
            return head
        mid = LinkedList.split_ll(head)
        right = LinkedList.merge_sort_helper(mid)
        left = LinkedList.merge_sort_helper(head)  # left
        return LinkedList.merge(left, right)

    @staticmethod
    def merge(left: Node, right: Node):
        dummy_head = Node('D')
        ptr = dummy_head
        while left and right:
            if left.data < right.data:
                ptr.nxt = left
                left = left.nxt
            else:
                ptr.nxt = right
                right = right.nxt

            ptr = ptr.nxt

        if left:
            ptr.nxt = left
        else:
            ptr.nxt = right

        return dummy_head.nxt

    def __repr__(self):
        return "[H]->{}".format(self.head)


if __name__ == '__main__':
    ll = LinkedList()
    ll.create_linked_list([4, 1, -3, 99, 5])
    print(ll)
    # ll.sort_bubble_dataxchnage()
    # ll.sort_bubble_linkxchange()
    ll.merge_sort()
    print(ll)
