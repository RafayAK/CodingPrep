'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each
node holding next and prev fields, it holds a field named both, which is an XOR of the next
node and the previous node. Implement an XOR linked list; it has an add(element) which adds the
element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access
to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''

"""
WARNING: DOESN'T ACTUALLY WORK CORRECTLY.
THE GARBAGE COLLECTOR REMOVES THE VALUE WHEN TRYING TO ACCESS IT.
AS A WORK AROUND TO TEST THE ALGO ALL THE NODES ARE STORED IN A SEPARATE LIST
SO THAT ACCESS IS POSSIBLE
"""


import _ctypes

class node:
    def __init__(self, data, tail_ptr):
        self.both = tail_ptr  # point to the previous element
        self.data = data

class XOR_linked_list:
    head_ptr= None # of the list head
    tail_ptr= None # tail of the list
    nodes_list = [] # NEED TO STORE ALL ELEMENTS SO THAT NODES PERSIST IN MEMORY AND ARE NOT REMOVED BY GARBAGE COLLECTTOR

    def __init__(self):
        pass


    def add(self,element):

        if XOR_linked_list.head_ptr is None and XOR_linked_list.tail_ptr is None:  # first element
            new_node = node(element, self.tail_ptr)
            XOR_linked_list.nodes_list.append(new_node)

            XOR_linked_list.head_ptr = self.get_pointer(new_node)  # store the memory address like a pointer of self
            XOR_linked_list.tail_ptr = self.get_pointer(new_node)  # store the memory address like a pointer of self
            new_node.both = 0  # attached to nothing
            #print(id(self))
            print('added first node')

        else:
            temp = node(element, self.tail_ptr)  # create new node
            temp_ptr = self.get_pointer(temp)
            XOR_linked_list.nodes_list.append(temp)
            # get the last node
            last_node = self.dereference_pointer(self.tail_ptr)

            last_node.both = last_node.both ^ temp_ptr  # XOR
            XOR_linked_list.tail_ptr = temp_ptr
            print('added {} to list'.format(element))




    def get(self, index):
        i = 0
        if i == index:
            return self.dereference_pointer(self.head_ptr).data
        if index== 19:
            temp = self.dereference_pointer(self.tail_ptr)
            return temp.data
        elif i < 0:
            return 'does not exist'
        else:

            current_ptr = self.head_ptr
            pre_ptr = 0  # to help traverse forward, always points one node back

            while(current_ptr != 0): # keep going forward until you reach the tail
                if i == index:

                    temp = self.dereference_pointer(current_ptr)
                    return temp.data

                link = self.dereference_pointer(current_ptr).both
                next_ptr = pre_ptr ^ link

                pre_ptr = current_ptr
                current_ptr = next_ptr
                i += 1

            return 'does not exist'

    def get_pointer(self, obj):
        return id(obj)

    def dereference_pointer(self, obj_id):
        """ Inverse of id() function. """
        return _ctypes.PyObj_FromPtr(obj_id)



if __name__ == '__main__':
    xor_list = XOR_linked_list()
    xor_list.add('A')
    xor_list.add('B')
    xor_list.add('C')
    xor_list.add('D')

    print(xor_list.get(2))