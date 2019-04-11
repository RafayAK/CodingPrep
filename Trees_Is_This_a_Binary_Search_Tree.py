""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

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

current_num = -1  # -1 appropriate as the constraints are >= 0
inorder = True
def check_inorder(root):
    global inorder
    global current_num
    if root.left:  # left exists
        check_inorder(root.left)

    if current_num < root.data:  # in-order
        current_num = root.data
    else:
        inorder = False
        return


    if root.right:
        check_inorder(root.right)



def checkBST(root):
    if not root: # root does not exist
        return
    check_inorder(root)
    if inorder:
        return True
    else:
        return False




if __name__ == '__main__':
    root = node(2)
    root.insert(1)
    root.insert(3)
    root.insert(2)

    #root = node(4)
    #root.create_my_tree()
    root.print_inorder()


    print(checkBST(root))
