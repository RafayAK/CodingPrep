"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
For example, in the following graph there is a cycle formed when node  points back to node .

image

Function Description

Complete the function has_cycle in the editor below.
It must return a boolean true if the graph contains a cycle, or false.

has_cycle has the following parameter(s):

: a pointer to a Node object that points to the head of a linked list.
Note: If the list is empty,  will be null.

Input Format

There is no input for this challenge. A random linked list is generated at runtime and passed to your function.

Constraints

Output Format

If the list contains a cycle, your function must return true.
If the list does not contain a cycle, it must return false.
The binary integer corresponding to
the boolean value returned by your function is printed to stdout by our hidden code checker.

Sample Input

The following linked lists are passed as arguments to your function:

1 -> NULL

1 -> 2 -> 3 -> 4 ->5 (loop from 5 to 3)
            \_____/
Sample Output

0
1
Explanation

The first list has no cycle, so we return false and the hidden code checker prints 1 to stdout.
The second list has a cycle, so we return true and the hidden code checker prints 0 to stdout.
"""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def print_list(node):
    while node:
        print(node.data, sep=" ", end= " ")
        node = node.next

    print() # just prints newline


def has_cycle(head):
    fast_ptr = head
    slow_ptr = head

    while fast_ptr.next and slow_ptr.next:

        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

        if fast_ptr == slow_ptr:
            # found loop
            return True

    return False

if __name__ == '__main__':
    llist = Node(1, next_node=Node(2, next_node=Node(3, next_node=Node(4, next_node=Node(5)))))
    llist.next.next.next.next.next = llist.next.next # set loop from 5 to 3


    print(has_cycle(llist))