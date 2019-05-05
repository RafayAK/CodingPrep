"""
You’re given the pointer to the head node of a linked list.
Change the next pointers of the nodes so that their order is reversed.
The head pointer given may be null meaning that the initial list is empty.

Input Format

You have to complete the SinglyLinkedListNode reverse(SinglyLinkedListNode head)
method which takes one argument - the head of the linked list. You should NOT read any input from stdin/console.

The input is handled by the code in the editor and the format is as follows:

The first line contains an integer , denoting the number of test cases.
Each test case is of the following format:

The first line contains an integer , denoting the number of elements in the linked list.
The next  lines contain an integer each, denoting the elements of the linked list.

Constraints

, where  is the  element in the list.
Output Format

Change the next pointers of the nodes that their order is reversed and return
the head of the reversed linked list. Do NOT print anything to stdout/console.

The output is handled by the code in the editor. The output format is as follows:

For each test case, print in a new line the elements of the linked list after reversing it, separated by spaces.
"""

class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def print_list(self):
        curr = self
        while(curr):
            print(curr.data, end=' ')
            curr = curr.next

        print()



def reverse_linked_list(head):
    a, b = None, head
    ptr_to_head = head

    while b is not None:
        temp = b.next
        b.next = a
        a = b
        b = temp

    ptr_to_head = a

    return ptr_to_head

if __name__ == '__main__':
    l = LinkedList(data=1, next=LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
    l.print_list()

    reversed_l = reverse_linked_list(l)
    reversed_l.print_list()
