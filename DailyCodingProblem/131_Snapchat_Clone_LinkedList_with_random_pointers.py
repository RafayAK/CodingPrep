"""
This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere
in the linked list, deep clone the list.
"""


class RandPtrNode:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt
        self.rand_ptr = None

    def __repr__(self):
        return "{}->{}".format(self.data, self.nxt)


def deep_copy(ll:RandPtrNode):

    # contains key: original_node
    #          value: new_deep_copied_node
    equivalent_node_dict = {}

    iter_a = ll  # iterator on the original linked list
    ll_copy = RandPtrNode(iter_a.data)  # create first node of the deep copied linked list
    iter_b = ll_copy  # iterator on the new linked list

    # add ll_copy's first node as equivalent of the original first node
    equivalent_node_dict[ll] = ll_copy

    iter_a = iter_a.nxt
    while iter_a:
        new_copied_node = RandPtrNode(iter_a.data)  # create new node

        # add new_copied_node as equivalent to the node currently pointed by iter_a
        equivalent_node_dict[iter_a] = new_copied_node

        # set next node to new_copied_node of the node currently pointed to by iter_b
        iter_b.nxt = new_copied_node

        # move iter_b to new_copied_node
        iter_b = new_copied_node

        iter_a = iter_a.nxt

    # reset iter pointers
    iter_a = ll
    iter_b = ll_copy

    # now set the rand pointer of the copied list by looking up
    # equivalent nodes in the dict

    while iter_a:
        if iter_a.rand_ptr:
            iter_b.rand_ptr = equivalent_node_dict[iter_a.rand_ptr]

        iter_a = iter_a.nxt
        iter_b = iter_b.nxt


    return ll_copy

if __name__ == '__main__':
    ll_with_rand = RandPtrNode(1, nxt=RandPtrNode(2, nxt=RandPtrNode(3)))
    ll_with_rand.rand_ptr = ll_with_rand  # 1 points to itself

    ll_with_rand.nxt.rand_ptr = ll_with_rand  # 2 points to 1
    ll_with_rand.nxt.nxt.rand_ptr = ll_with_rand  # 3 points to 1

    ll_with_rand_copy = deep_copy(ll_with_rand)

    # tests
    # print(ll_with_rand_copy.rand_ptr)
    # print(ll_with_rand_copy.nxt.rand_ptr)
    # print(ll_with_rand_copy.nxt.nxt.rand_ptr)

    assert ll_with_rand_copy.rand_ptr.data == 1
    assert ll_with_rand_copy.nxt.rand_ptr.data == 1
    assert ll_with_rand_copy.nxt.nxt.rand_ptr.data == 1
