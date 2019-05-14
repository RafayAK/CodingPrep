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

def print_doubly_linked_list(node, sep=' ', end=' '):
    while node:

        print(node.data, sep=sep, end=end)
        node = node.next

    print(end='\n')


def sortedInsert(head, data):

    # define new node
    new_node = DoublyLinkedListNode(node_data=data)

    if data < head.data:
        head.prev = new_node
        new_node.next = head
        head = new_node
        return head

    curr_node = head.next
    prev_node = head
    while curr_node:
        if curr_node.data > data >= curr_node.prev.data:
            new_node.prev = curr_node.prev
            new_node.next = curr_node
            curr_node.prev.next = new_node
            curr_node.prev = new_node
            return head

        prev_node = curr_node
        curr_node = curr_node.next

    prev_node.next = new_node
    new_node.prev = prev_node

    return head


if __name__ == '__main__':

    llist = DoublyLinkedList()
    llist.insert_node(1)
    llist.insert_node(3)
    llist.insert_node(4)
    llist.insert_node(10)

    print_doubly_linked_list(llist.head)

    llist_head = sortedInsert(llist.head, 4)

    print_doubly_linked_list(llist_head)

    llist_head = sortedInsert(llist.head, 5)

    print_doubly_linked_list(llist_head)

    llist_head = sortedInsert(llist.head, 0)

    print_doubly_linked_list(llist_head)

    llist_head = sortedInsert(llist.head, 10)

    print_doubly_linked_list(llist_head)
