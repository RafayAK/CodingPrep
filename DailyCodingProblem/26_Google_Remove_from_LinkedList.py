'''
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next= next

class LinkedList:
    def __init__(self):
        self.start= None
        self.end = None

    def add(self, data=None):

        new_node = node(data) # create new node to add

        if self.start is None and self.end is None:
            # empty list create first node
            self.start = new_node
            self.end = new_node
        else:
            # add node to the end of the list
            self.end.next = new_node
            self.end = new_node # change pointer to this

    def print_list(self):
        curr_node = self.start
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next


def remove_k_last_item(linked_list, k):
    iter_counter = 0
    temp_ptr = None # this pointer points to k+1 last elemnt i.e if K=2nd last element then temp=3rd last element
    k_last_element = None
    it = linked_list.start # set iterator to start of list
    while it is not None:
        if k -iter_counter == 0:
            k_last_element = linked_list.start
        elif k_last_element is not None:
            # k_last_element was set some time before
            temp_ptr = k_last_element # set temp_ptr before going forward
            k_last_element = k_last_element.next

        it = it.next
        iter_counter += 1

    # now delete the k-last element
    if k_last_element == linked_list.end:
        temp_ptr.next = None
        linked_list.end = temp_ptr
    else:
        temp_ptr.next = k_last_element.next

    del k_last_element
    return linked_list

if __name__ == '__main__':
    linked_list = LinkedList()
    # create list of the following structure: 1->2->3->4
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)

    print("original list:")
    linked_list.print_list()

    k = 0
    linked_list = remove_k_last_item(linked_list, k)
    print("list after removing {} last element form the list".format(k))
    linked_list.print_list()