"""
ou’re given the pointer to the head node of a linked list, an integer to add
to the list and the position at which the integer must be inserted.
Create a new node with the given integer, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.
The head pointer given may be null meaning that the initial list is empty.

As an example, if your list starts as  and you want to insert a node at position  with , your new list should be

Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference
to the head node of your finished list.

insertNodeAtPosition has the following parameters:

head: a SinglyLinkedListNode pointer to the head of the list
data: an integer value to insert as data in your new node
position: an integer position to insert the new node, zero based indexing
Input Format

The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
The last line contains an integer .

Constraints

, where  is the  element of the linked list.
.
Output Format

Return a reference to the list head. Locked code prints the list for you.

Sample Input

3
16
13
7
1
2
Sample Output

16 13 1 7
Explanation

The initial linked list is 16 13 7. We have to insert  at the position  which currently has
in it. The updated linked list will be 16 13 1 7
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep=' ', end=' '):
    while node:
        print(node.data, sep=sep, end=' ')
        node = node.next

    print(end='\n')


# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.
# The head pointer given may be null meaning that the initial list is empty.
def insertNodeAtPosition(head, data, position):
    # set position to be given_position -1
    position = position -1

    # define new node
    new_node = SinglyLinkedListNode(node_data=data)

    if head is None:
        head = new_node

    if position == -1:
        # then set head to be new data
        new_node.next = head
        head = new_node

    curr_node = head
    counter = 0
    while curr_node:
        if counter == position:
            new_node.next = curr_node.next
            curr_node.next = new_node
            break
        counter+=1
        curr_node = curr_node.next




    return head

if __name__ == '__main__':
    llist = SinglyLinkedList()

    llist.insert_node(16)
    llist.insert_node(13)
    llist.insert_node(7)

    print_singly_linked_list(llist.head)
    llist_head = insertNodeAtPosition(llist.head, 4, 2)
    print_singly_linked_list(llist_head)



