'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

"""
Assuming some thing like this
list1 = 1->2->3->7->8->10
list2 = 99->1->8->10

so visualizing:
 1  
  2  
   3
     7
99->1->8->10

"""


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def print_list(list):
    if list is None:
        return
    print(list.data)
    print_list(list.next)


def find_intersection(list1, list2):# O(M*K)

    pointerL2 = list2

    while pointerL2:
        pointerL1 = list1
        while pointerL1:
            if pointerL1 == pointerL2:  # found intersection
                return pointerL1.data
            pointerL1 = pointerL1.next
        pointerL2 = pointerL2.next


def find_intersection_2(list1, list2):# O(M+K)
    #  idea store pointer values to a dictionar
    # return when match found
    dict_visited = {}  # dict of visited nodes

    pointer = list1

    while pointer:
        dict_visited[id(pointer)] = None  # just add the key no need to store a value
        pointer = pointer.next

    pointer = list2
    while pointer:
        if id(pointer) in dict_visited:
            return ('intersection point at: {}'.format(pointer.data))
        pointer = pointer.next

    return 'No Intersection'




if __name__ == '__main__':
    common_tail = LinkedList(8, next=LinkedList(10))
    l1 = LinkedList(1, next=LinkedList(2,next=LinkedList(3, next=LinkedList(7, next=common_tail))))
    l2 = LinkedList(99, next=LinkedList(1, next=common_tail))

    # print_list(l1)
    # print('\n')
    # print_list(l2)
    # print('\n')
    print(find_intersection_2(l1,l2))

