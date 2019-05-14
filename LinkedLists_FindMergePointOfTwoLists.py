"""
Given pointers to the head nodes of  linked lists that merge together at some point,
find the Node where the two lists merge. It is guaranteed that the two head Nodes will
be different, and neither will be NULL.

In the diagram below, the two lists converge at Node x:

[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q

Complete the int `findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2)`
method so that it finds and returns the data value of the Node where the two lists merge.

Input Format:

Do not read any input from stdin/console.

The findMergeNode(SinglyLinkedListNode,SinglyLinkedListNode) method has two parameters,
and , which are the non-null head Nodes of two separate linked lists that are guaranteed to converge.

Constraints

The lists will merge.
head1, head2 != NULL
head1 != head2

Output Format

Do not write any output to stdout/console.

Each Node has a data field containing an integer. Return the integer data for the Node where the two lists merge.

Sample Input

The diagrams below are graphical representations of the lists that input Nodes  and  are connected to.
Recall that this is a method-only challenge; the method only has initial visibility to those  Nodes
and must explore the rest of the Nodes using some algorithm of your own design.

Test Case 0

 1
  \
   2--->3--->NULL
  /
 1
Test Case 1

1--->2
      \
       3--->Null
      /
     1
Sample Output

2
3
Explanation

Test Case 0: As demonstrated in the diagram above, the merge Node's data field contains the integer 2.
Test Case 1: As demonstrated in the diagram above, the merge Node's data field contains the integer 3.
"""

# !/bin/python3

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


def print_singly_linked_list(node, sep=" ", end=" "):
    while node:
        print(node.data, sep=sep, end=end)

        node = node.next

    print(end='\n')


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2): # O(N) time, O(N) space
    # idea: store pointers to list as keys in a dictionary

    pointers_dict = {}

    node_iter1 = head1
    node_iter2 = head2

    while node_iter1:
        pointers_dict[node_iter1] = None  # only need the keys
        node_iter1 = node_iter1.next

    while node_iter2:
        if node_iter2 in pointers_dict:
            return node_iter2.data

        node_iter2 = node_iter2.next

    return None


# brilliantly simple sol:
# IDEA: lets say len(list2) + len(list2) = X
#       then if we start two pointers at each list and then swap them to the start of the opposite list
#       when they bottom out their list's, then both the pointers would have moved the same distance when
#       they meat at the intersection point

# eg :
# list1 = 1->2->3
# list2 = 1->3
# intersection point is 3
#
#   ptr1 : 1->2->3--(switch to list2)-->1->3 (5 steps)
#   ptr2 : 1->3--(switch to list2)-->1->2->3 (5 steps)
#
#
# convergence should be guaranteed, otherwise will get stuck in loop
def findMergeNode2(head1, head2): # O(N) time O(1) space
    node_iter1 = head1
    node_iter2 = head2

    while node_iter1 != node_iter2:

        if node_iter1.next is None:
            node_iter1 = head2
        else:
            node_iter1 = node_iter1.next

        if node_iter2.next is None:
            node_iter2 = head1
        else:
            node_iter2 = node_iter2.next

    return node_iter1.data  # return data of intersecting point


if __name__ == '__main__':

    # test case 0
    # list1 = SinglyLinkedList()
    # list1.insert_node(1)
    # list1.insert_node(2)
    # list1.insert_node(3)
    #
    # print_singly_linked_list(list1.head)
    #
    # list2 = SinglyLinkedList()
    # list2.insert_node(1)
    # list2.head.next = list1.head.next

    # print_singly_linked_list(list2.head)


    # test case 1
    list1 = SinglyLinkedList()
    list1.insert_node(1)
    list1.insert_node(2)
    list1.insert_node(3)

    print_singly_linked_list(list1.head)

    list2 = SinglyLinkedList()
    list2.insert_node(1)
    list2.head.next = list1.head.next.next

    print_singly_linked_list(list2.head)

    print(findMergeNode(list1.head, list2.head))

