"""
This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""


class Node:
    def __init__(self, data, nxt = None):
        self.data = data
        self.nxt = nxt

    def __repr__(self):
        return "{}->{}".format(self.data, self.nxt)


def combine_lls(lls: list):
    new_ll = None
    tail = None

    while lls:  # run until the list of pointers is empty
        min_head = min(lls, key=lambda x: x.data)  # get min_pointer based on the data vlaue
        min_value = min_head.data  # get the data value from the pointer
        min_values_idx = lls.index(min_head)  # get the index where the min_head was found

        if new_ll is None:
            new_ll = Node(data=min_value)
            tail = new_ll
        else:
            tail.nxt = Node(min_value)
            tail = tail.nxt

        lls[min_values_idx] = lls[min_values_idx].nxt  # move the pointer of this linked_list to the next element

        if lls[min_values_idx] is None:  # if after moving the linked_list points to None, remove it
            del lls[min_values_idx]

    return new_ll


if __name__ == '__main__':

    # test 1
    ll_1 = Node(1, nxt=Node(4, nxt=Node(8)))
    ll_2 = Node(2, nxt=Node(5, nxt=Node(9)))
    ll_3 = Node(3, nxt=Node(6, nxt=Node(7)))

    res = combine_lls([ll_1, ll_2, ll_3])

    print(res)  # 1->2->3->4->5->6->7->8->9->None

    # test 2
    ll_1 = Node(1, nxt=Node(2, nxt=Node(3)))
    ll_2 = Node(2, nxt=Node(3, nxt=Node(4)))
    ll_3 = Node(3, nxt=Node(4, nxt=Node(5)))
    ll_4 = Node(4, nxt=Node(5, nxt=Node(6)))

    res = combine_lls([ll_1, ll_2, ll_3, ll_4])

    print(res)  # 1->2->2->3->3->3->4->4->4->5->5->6->None

    # test 3
    ll_1 = Node(1, nxt=Node(4, nxt=Node(6)))
    ll_2 = Node(2, nxt=Node(3, nxt=Node(9)))
    ll_3 = Node(1, nxt=Node(3, nxt=Node(7)))

    res = combine_lls([ll_1, ll_2, ll_3])

    print(res)  # 1->2->2->3->3->3->4->4->4->5->5->6->None
