"""
You’re given the pointer to the head node of a doubly linked list.
Reverse the order of the nodes in the list. The head node might be NULL to
indicate that the list is empty. Change the next and prev pointers of all the
nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Function Description

Complete the reverse function in the editor below. It should return a reference to the head of your reversed list.

reverse has the following parameter(s):

head: a reference to the head of a DoublyLinkedList
Input Format

The first line contains an integer , the number of test cases.

Each test case is of the following format:

The first line contains an integer , the number of elements in the linked list.
The next  lines contain an integer each denoting an element of the linked list.
Constraints

Output Format

Return a reference to the head of your reversed list.
The provided code will print the reverse array as a one line of space-separated integers for each test case.

Sample Input

1
4
1
2
3
4
Sample Output

4 3 2 1
Explanation

The initial doubly linked list is: 1<->2<->3<->4<->NULL

The reversed doubly linked list is: 4<->3<->2<->1<->NULL
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node


def print_doubly_linked_list(node, sep=" ", end =" "):
    while node:
        print(node.data, sep=sep, end=end)

        node = node.next

    print(end='\n')

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    a, b = None, head

    while b:
        temp = b.next
        b.next = a
        b.prev = temp
        a = b
        b = temp

    head = a
    return head



if __name__ == '__main__':

    llist = DoublyLinkedList()
    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)
    llist.insert_node(4)

    print_doubly_linked_list(llist.head)

    reversed_llist = reverse(llist.head)
    print_doubly_linked_list(reversed_llist)
