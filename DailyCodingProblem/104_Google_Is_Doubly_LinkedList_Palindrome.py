"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False."""

# works for both singly and doubly linked lists

class LinkedList:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def __repr__(self):
        return "{}->{}".format(self.data, self.nxt)


def is_ll_palindrome(head):
    # store the Linked list into a string
    string = ""
    # traverse linked list
    curr = head
    while curr:
        string = string + str(curr.data)
        curr = curr.nxt

    temp = string[::-1]

    return string == string[::-1]


# basically this is storing the pointer to the elements of the linked list in a call stack
def is_ll_palindrome_redux(head):
    left = head

    def helper(right):
        nonlocal left
        if right.nxt is None:
            return left.data == right.data

        if helper(right.nxt) is False:
            return False
        left = left.nxt
        return left.data == right.data

    return helper(head)


if __name__ == '__main__':
    ll1 = LinkedList('a', nxt=LinkedList('b', nxt=LinkedList('c', nxt=LinkedList('b', nxt=LinkedList('a')))))

    print(is_ll_palindrome_redux(head=ll1))
