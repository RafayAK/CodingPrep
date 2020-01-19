"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number.
The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""

class node:
    def __init__(self, val, nxt=None):
        self.nxt = nxt
        self.val = val

    def __repr__(self):
        return "{}".format(self.val)

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_val(self, val):
        if self.head is None and self.tail is None:
            self.head = node(val)
            self.tail = self.head
        else:
            self.tail.nxt = node(val)
            self.tail = self.tail.nxt

    def __repr__(self):
        string = ""

        def helper(curr):
            nonlocal string
            if curr:
                helper(curr.nxt)
                string = string + "{}".format(curr)

        helper(self.head)
        return string


def sum_ll(ll1:linkedList, ll2:linkedList):
    res_ll = linkedList()

    iter_1, iter_2 = ll1.head, ll2.head
    carry = 0
    tail = res_ll
    while iter_1 is not None and iter_2 is not None:
        s = iter_1.val + iter_2.val +carry

        if s > 9:
            carry = 1
            s = s -10

            res_ll.add_val(s)
        else:
            res_ll.add_val(s)
            carry =0

        iter_1 = iter_1.nxt
        iter_2 = iter_2.nxt

    while iter_2 is not  None:
        s = iter_2.val + carry

        if s > 9:
            carry = 1
            s = s - 10

            res_ll.add_val(s)
        else:
            res_ll.add_val(s)
            carry = 0

        iter_2 = iter_2.nxt

    while iter_1 is not None:
        s = iter_1.val + carry

        if s > 9:
            carry = 1
            s = s - 10

            res_ll.add_val(s)
        else:
            res_ll.add_val(s)
            carry = 0

        iter_1 = iter_1.nxt

    return res_ll


if __name__ == '__main__':
    ll1 = linkedList()  # 29
    ll1.add_val(9)
    ll1.add_val(2)

    ll2 = linkedList()  # 544
    ll2.add_val(4)
    ll2.add_val(4)
    ll2.add_val(5)

    print(sum_ll(ll1, ll2))