"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

eg.
                    5
                  /  \
                2     6
               / \     \
              1   4     9
                /        \
               3         12
                        /
                       11

               ANS = 11

eg.
              5
            /  \
           2    8

           ANS = 5

eg.             6
               /
              4
            /  \
           3    5

           ANS = 5

NOTICE: ANS is either:
        1- the root-node,
        2- in the right sub-tree from the root-node, if it exists
        3- in the left subtree from the root node.

"""


class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right= right

    def create_my_tree(self): # ANS False
        self.data = 4
        self.left = node(2)
        self.right= node(6)

        self.left.left=node(1)
        self.left.right = node(2)

        self.right.left = node(5)
        self.right.right = node(7)

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
                self.left = node(data)
            else: # left exists
                self.left.insert(data)
        else: # add to the right
            if self.right == None: # right empty
                self.right = node(data)
            else: # right exists
                self.right.insert(data)



def find_second_largest(root:node):
    arr = [] # stores in the 0th position the second largest element and in the 1st position the largest one

    arr.append(root.data) # the 1st condition

    # if right subtree exists
    if root.right:

        def search_right(current_node):
            if current_node.left:  # left exists -> go left
                search_right(current_node.left)

            if len(arr) == 1:
                if current_node.data < arr[0]:
                    arr.insert(0, current_node.data)
                else:
                    arr.insert(1, current_node.data)
            elif len(arr) == 2:
                if current_node.data > arr[1]:
                    arr[0], arr[1] = arr[1], arr[0]
                    arr[1] = current_node.data

            if current_node.right:  # left exists -> go left
                search_right(current_node.right)

        current_node = root.right
        search_right(current_node)
        return arr[0]

    # only left subtree exists

    def search_left(current_node):
        if current_node.left: # left exists -> go left
            search_left(current_node.left)


        # check if smaller or bigger
        if len(arr) ==1:
            if current_node.data < arr[0]:
                arr.insert(0, current_node.data)
            else:
                arr.insert(1, current_node.data)
        elif len(arr) == 2:
            # in the left subtree the elements can't be bigger than the root
            if current_node.data > arr[0]:
                arr[0]=current_node.data

        if current_node.right:
            search_left(current_node.right)

    current_node = root.left
    search_left(current_node)
    return arr[0]



if __name__ == '__main__':
    # tree = node(5,
    #             left=node(2, left=node(1), right=node(4, left=node(3))),
    #             right=node(6, right=node(9, right=node(12, left=node(11))))) # ans 11

    # tree = node(5,
    #             left=node(2),
    #             right=node(8)) # ans 5

    # tree = node(6,
    #             left=node(4, left=node(3), right=node(5))) # ans 5

    tree = node(9,
                left=node(4, left=node(1)),
                right=node(7, right=node(31, left=node(14),right=node(82)))) # ans 31

    print(find_second_largest(tree))