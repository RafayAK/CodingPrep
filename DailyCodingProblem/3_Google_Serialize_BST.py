'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

    def print_node(self):
        print(self.data)

    def print_inorder(self):
        if self.left:  # left exists
            self.left.print_inorder()

        print(self.data)

        if self.right:
            self.right.print_inorder()

    def insert(self, data):
        if (data <= self.data): # add to the left
            if self.left == None: # left empty
                self.left = Node(data)
            else: # left exists
                self.left.insert(data)
        else: # add to the right
            if self.right == None: # right empty
                self.right = Node(data)
            else: # right exists
                self.right.insert(data)


def serialize(root): # using pre-order traversal -> root,left,right
    serialized_tree = []
    def helper(node):
        if node is None: # root does not exist
            return []

        serialized_tree.append(node.val)

        if node.left:
            helper(node.left)
        else:
            serialized_tree.append('?')

        if node.right:
            helper(node.right)
        else:
            serialized_tree.append('?')

    helper(root)
    return serialized_tree

def deserialize(ls): # takes a list to construct a tree
    listIter = iter(ls)
    def helper():
        val = next(listIter)
        if val == '?':
            return None
        else:
            node = Node(val)
            node.left = helper()
            node.right = helper()
            return node

    return helper()



if __name__ == '__main__':
    #root = Node(20,Node(8),Node(22))
    #root = Node(20, left= Node(8), right=Node(22))
    root = Node('root', Node('left', Node('left.left')), Node('right'))
    ls = serialize(root)
    print(ls)
    assert deserialize(serialize(root)).left.left.val == 'left.left'

