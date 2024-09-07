'''
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be
locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    1-  is_locked(), which returns whether the node is locked

    2-  lock(), which attempts to lock the node.
        If it cannot be locked, then it should return false.
        Otherwise, it should lock it and return true.

    3-  unlock(), which unlocks the node. If it cannot be unlocked, then it should return false.
        Otherwise, it should unlock it and return true.


You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for
actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
'''


class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self._is_locked = False
        self.parent_ptr = parent
        self._locked_descendants_count = 0


    def _can_lock_or_unlock(self):
        if self._locked_descendants_count > 0:
            return False

        curr = self.parent_ptr
        while curr:
            if curr._is_locked:
                return False
            curr = curr.parent_ptr
        return True

    def is_locked(self):
        return self._is_locked

    # searches fot the node's children and parents for a is_locked=True
    def lock(self):
        if self._can_lock_or_unlock():
            if self.is_locked():
                # already locked
                print("Node already locked")
                return False

            # not locked, so we can set _is_locked=True and update count in all ancestors
            self._is_locked = True

            curr = self.parent_ptr
            while curr:
                curr._locked_descendants_count+=1
                curr = curr.parent_ptr

            print("Success! Node locked")
            return True
        else:
            print("Failed! Node cannot be locked")
            return False

    def unlock(self):
        if self._can_lock_or_unlock():
            # we can unlock this node

            if self._is_locked is False: # check if it need to be unlocked
                print("Node already unlocked")
                return False

            self._is_locked = False

            # update count is all ancestors
            curr = self.parent_ptr
            while curr:
                curr._locked_descendants_count -= 1
                curr = curr.parent_ptr
            print("Success! Node unlocked")
            return True
        else:
            print("Failed! Node cannot be locked")
            return False


    def add_node(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data, parent=self)
            else:
                self.left.add_node(data)
        else:
            if self.right is None:
                self.right = Node(data, parent=self)
            else:
                self.right.add_node(data)


if __name__ == '__main__':

    """
    This is the created tree    
                3
               / \
              1   4
             /     \
            0       5
    """

    root_locking_tree = Node(3)

    root_locking_tree.add_node(1)
    root_locking_tree.add_node(4)
    root_locking_tree.add_node(0)
    root_locking_tree.add_node(5)


    # try to  unlock leaf node 5, its already unlocked
    node_to_lock_1 = root_locking_tree.right.right
    node_to_lock_1.unlock()

    # try to  unlock leaf node 5, should Succeed
    node_to_lock_1.lock()

    # try locking root node, should Fail
    root_locking_tree.lock()

    # try unlocking root node, should Fail
    root_locking_tree.unlock()

    # try locking node 1, should succeed
    node_to_lock_2 = root_locking_tree.left
    node_to_lock_2.lock()

    # unlock leaf node 5, should succeed
    node_to_lock_1.unlock()

    # now try lock node 1, already locked
    node_to_lock_2.lock()

    # try locking root node, should Fail
    root_locking_tree.lock()




